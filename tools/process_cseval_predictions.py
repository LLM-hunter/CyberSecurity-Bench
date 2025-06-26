'''
使用大模型根据'origin_prompt'从'prediction'中提取格式化答案。

不同的模型可能会导致答案提取的略微差异，能力越强的模型，答案提取效果越好，得分也越准确

使用方法：
python cseval.py input_file output_file

input_file: 输入的JSON文件路径 (例如: results/cseval/SecGPT-7B/secgpt_7b_cseval.json)
output_file: 输出的JSON文件路径 (例如: secgpt_7b_cseval_extract.json)
'''
import requests
import json
import datetime
import re
import pandas as pd
import argparse

# --- 配置区 ---
MODEL_API_URL = "your_model_api_url"  # 模型API地址
MODEL_NAME = "your_model_name"  # 模型名称
# 更新SYSTEM_PROMPT以反映其作为提取专家的角色
SYSTEM_PROMPT = """你是一个信息提取专家。你的任务是根据"原始提示"中的要求，从"预测内容"中提取出格式完全一致的答案。
规则：
1.  仔细分析"原始提示"，理解题目类型（例如：单选、多选、判断、知识抽取等）以及要求的答案格式。
2.  严格按照"原始提示"的格式要求，从"预测内容"中提取核心答案。
3.  不要修正或猜测答案的正确性。如果预测内容是错误的，你也需要按格式要求提取出来。
4.  如果"预测内容"包含"答案是"、"选项是"或者任何解释性文字，请忽略它们。
5.  对于多选题，将所有选项字母连接成一个无空格、无逗号的字符串，并按字母顺序排序（例如：ACD）。
6.  对于单选题，只返回单个字母。
7.  对于判断题，根据提示要求返回"是"/"否"或"对"/"错"或"YES"/"NO"。
8.  如果“预测内容”中找不到任何符合格式要求的答案，或内容含糊不清（例如：“可能是A或者B”），则返回一个空字符串
9.  最终输出除了提取的答案外，不应包含任何其他字符。"""
TEMPERATURE = 0.1  # 降低温度以获得更确定的输出
TOP_P = 0.1
MAX_TOKENS = 2048 # 适当增加以处理更长的prompt
REQUEST_TIMEOUT = 120


def compare_json_semantics(data_list, prompt, file_name, question_key, fine_query_key):
    """
    比较data_list中每个JSON对象的question和fine_query字段，并将结果存入JSONL文件。

    参数：
    data_list (list): 包含JSON对象的列表。
    prompt (str): 用于比较的提示语。
    file_name (str): 保存结果的文件名。
    question_key (str): 用于获取question的字段名。
    fine_query_key (str): 用于获取fine_query的字段名。
    """
    with open(file_name, 'w', encoding='utf-8') as f:
        for data in data_list:
            question = data.get(question_key)
            fine_query = data.get(fine_query_key)
            
            if question is not None and fine_query is not None:
                # 使用传入的prompt并插入实际的question和fine_query值
                formatted_prompt = prompt.format(question=question, text=fine_query)
                print(formatted_prompt)
                data = {
                    "model": MODEL_NAME,
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": formatted_prompt}
                    ],
                    "temperature": TEMPERATURE,
                    "top_p": TOP_P,
                    "max_tokens": MAX_TOKENS
                }
                try:
                    response = requests.post(MODEL_API_URL, json=data, timeout=REQUEST_TIMEOUT)
                    response.raise_for_status()
                    result = response.json()
                    # 打印模型的原始输出
                
                    # 提取模型的回答并使用正则表达式提取'true'或'false'
                    answer = result['choices'][0]['message']['content'].strip().lower()
                    match = re.search(r'\b(true|false)\b', answer)
                    result_value = match.group(0) if match else 'unknown'
                    # 存入JSONL文件
                    jsonl_content = {"question": question, f"{fine_query_key}": fine_query,"result": result_value}
                    f.write(json.dumps(jsonl_content, ensure_ascii=False) + "\n")
                except requests.exceptions.RequestException as e:
                    print(f"请求失败: {e}")

def read_jsonl(file_path):
    """
    读取JSONL文件并返回每一行的JSON对象列表。

    参数：
    file_path (str): JSONL文件的路径。

    返回：
    list: 包含每一行JSON对象的列表。
    """
    data_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    data = json.loads(line)
                    data_list.append(data)
                except json.JSONDecodeError as e:
                    print(f"JSON解码错误: {e}")
    except FileNotFoundError:
        print(f"文件{file_path}不存在。")
    return data_list

def read_json(file_path):
    """
    读取JSON文件并返回内容。

    参数：
    file_path (str): JSON文件的路径。

    返回：
    dict: JSON文件的内容，失败则返回空字典。
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"错误: 文件 {file_path} 不存在。")
        return {}
    except json.JSONDecodeError as e:
        print(f"错误: JSON文件 {file_path} 解码失败: {e}")
        return {}

def extract_data(json_data):
    """
    从 JSON 数据中提取每个 JSON 对象的 origin_prompt 和 prediction 字段。
    question_id 从 1 开始。

    参数：
    json_data (dict): 包含多个 JSON 对象的字典。

    返回：
    list: 包含 (question_id, origin_prompt, prediction) 元组的列表。
    """
    data_items = []
    # 遍历 JSON 数据中的每个键值对
    for key, obj in json_data.items():
        if 'origin_prompt' in obj and 'prediction' in obj:
            try:
                # question_id 从 1 开始
                question_id = int(key) + 1
                origin_prompt = obj['origin_prompt']
                prediction = obj['prediction']
                data_items.append((str(question_id), origin_prompt, prediction))
            except (ValueError, TypeError):
                print(f"警告: 键 '{key}' 不是有效数字，已跳过。")
                continue
        else:
            print(f"警告：键 '{key}' 对应的 JSON 对象中缺少 'origin_prompt' 或 'prediction' 字段，已跳过。")
    
    # 按 question_id 排序
    data_items.sort(key=lambda x: int(x[0]))
    return data_items

def process_with_model(data_items, output_file):
    """
    使用模型处理预测结果并提取答案。

    参数：
    data_items (list): 包含(question_id, origin_prompt, prediction)元组的列表。
    output_file (str): 输出文件名。
    """
    results = []
    
    for i, (qid, origin_prompt, pred) in enumerate(data_items):
        prompt = f"""原始提示:
---
{origin_prompt}
---

预测内容:
---
{pred}
---

提取的答案:"""
        
        data = {
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            "temperature": TEMPERATURE,
            "top_p": TOP_P,
            "max_tokens": MAX_TOKENS
        }
        
        try:
            response = requests.post(MODEL_API_URL, json=data, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            result = response.json()
            answer = result['choices'][0]['message']['content'].strip()
            
            # 即使有强大的prompt，也保留一个简单的清理作为后备
            answer = answer.replace('"', '').replace("'", "").strip()
            
            result_item = {
                "question_id": int(qid),
                "answer": answer
            }
            results.append(result_item)
            
            print(f"已处理第 {i+1}/{len(data_items)} 条 (Question ID: {qid}) -> 提取到答案: '{answer}'")
            
        except requests.exceptions.RequestException as e:
            print(f"请求失败 (Question ID: {qid}): {e}")
            result_item = {
                "question_id": int(qid),
                "answer": "处理失败"
            }
            results.append(result_item)
            
    return results

def save_results_to_json(results, output_file):
    """
    将结果保存为JSON文件。

    参数：
    results (list): 结果列表
    output_file (str): 输出文件名
    """
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=4)
        print(f"\n提取完成！结果已保存到 {output_file}")
    except IOError as e:
        print(f"\n错误：无法写入文件 {output_file}: {e}")

# 主程序入口
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="使用大模型根据'origin_prompt'从'prediction'中提取格式化答案。")
    parser.add_argument("input_file", help="输入的JSON文件路径 (例如: results/cseval/SecGPT-7B/secgpt_7b_cseval.json)")
    parser.add_argument("output_file", help="输出的JSON文件路径 (例如: secgpt_7b_cseval_extract.json)")
    args = parser.parse_args()

    print(f"正在从 {args.input_file} 读取数据...")
    json_data = read_json(args.input_file)
    
    if json_data:
        data_to_process = extract_data(json_data)
        print(f"成功提取 {len(data_to_process)} 条数据项，准备使用模型进行处理...")
        
        results = process_with_model(data_to_process, args.output_file)
        
        save_results_to_json(results, args.output_file)
    else:
        print("未能读取或解析输入文件，程序退出。")