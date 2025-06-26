# CyberSecurity-Bench 开源安全评测社区

### 专注于安全AI模型的开源评测平台

[🚀快速开始](#-快速开始) |
[📚知识库管理](#-知识库管理) |
[🧪评测框架](#-评测框架) |
[📊结果展示](#-结果展示) |
[🐛常见问题](#-常见问题)

## 📁 项目结构

```bash
CyberSecurity-Bench/
├── README.md                       # 项目说明文档
├── data/                           # 标准化安全数据集
│   ├── cissp/                      # CISSP信息安全题库
│   ├── cisco/                      # 思科威胁情报数据
│   └── cseval/                     # CS-Eval计算机安全
├── evaluation/                     # 评测脚本与工具
│   ├── cisco/                      # 思科威胁情报评测配置
│   │   ├── cti_mcq_judge.py        # CTI多选题评测脚本
│   │   └── cti_rcm_judge.py        # CTI案例评测脚本
│   └── cissp/                      # CISSP信息安全配置
│       └── cissp_judge.py          # CISSP评测脚本
├── models/                         # 模型配置模板
│   └── configs/                    # OpenCompass兼容配置
│       ├── api_models/             # API模型配置
│       └── local_models/           # 本地模型配置
├── tools/                          # 辅助工具
└── results/                        # 评测结果与分析
```

## 🌟 项目简介

**CyberSecurity-Bench** 是一个专注于安全领域的开源模型评测平台，致力于为安全AI模型的评估提供全面的解决方案。通过标准化评测框架和结构化的安全知识库体系，CyberSecurity-Bench能够：

- 🎯 **深度评估模型安全能力**：针对漏洞识别、合规分析、威胁预测等专业领域提供专项评测
- 📚 **集成多维知识库**：构建网络安全、行业合规、漏洞数据库等专业安全知识体系
- 🔧 **提供标准化评测工具**：开箱即用的评测脚本与可视化分析工具
- 📈 **驱动模型迭代优化**：通过量化指标与案例对比展示模型能力演进
- 🤝 **社区驱动发展**：开放的知识库贡献机制，共建安全AI评测生态

> 🎯 **平台使命**: 建立安全AI模型评测的行业标准，推动安全领域人工智能技术的发展与应用

### ✨ 核心特性

- **🏆 标准化评测**：基于OpenCompass框架的专业评测体系
- **📊 多维度分析**：从技术能力到实战应用的全方位评估
- **🔄 持续更新**：社区驱动的知识库动态扩展机制
- **🎯 领域专精**：专注安全领域的深度评测与分析
- **🌐 开放生态**：完全开源，支持自定义扩展与贡献

## 📚 知识库管理

CyberSecurity-Bench 提供多层次的安全知识库体系，涵盖从基础概念到前沿威胁的全方位内容：

### 🔒 安全专业知识库

| 知识库类型 | 数据集名称 | 描述 | 题目数量 | 更新时间 |
|------------|------------|------|----------|----------|
| **网络安全基础** | CS-Eval | 网络安全综合评测 | 4000+ | 2025/6/18 |
| **安全认证** | CISSP | 信息安全综合评测 | 2000+ | 2025/6/18  |
| **漏洞分析** | CTI-MCQ | 威胁情报选择题 | 2000+ | 2025/6/18  |
| **威胁响应** | CTI-RCM | 威胁响应分析题 | 1000+ | 2025/6/18  |

### 🌐 通用能力基准

| 知识库类型 | 数据集名称 | 描述 | 评测目的 |
|------------|------------|------|----------|
| **数学推理** | GSM8K | 数学问题求解数据集 | 基础逻辑能力 |
| **综合知识** | MMLU | 多领域知识评测 | 知识广度测试 |
| **复杂推理** | BBH | 复杂语言理解能力 | 推理能力极限 |
| **中文理解** | C-Eval | 中文综合能力 | 中文处理能力 |

### 🚀 即将推出

- **🛡️ 恶意软件分析**：恶意代码识别与分析评测
- **🔐 密码学应用**：密码算法与协议安全评测  
- **🌐 Web安全**：Web应用安全漏洞检测评测
- **☁️ 云安全**：云环境安全配置与防护评测
- **📱 移动安全**：移动应用安全分析评测

> 💡 **数据集扩展**: 我们将持续与安全行业专家合作，定期更新和扩展知识库内容

## 🚀 快速开始

### 📋 环境要求

- **操作系统**: Linux / macOS / Windows
- **Python**: 3.10 或更高版本
- **CUDA**: 11.8+ (如需 GPU 加速)
- **内存**: 建议 16GB 以上
- **存储**: 至少 10GB 可用空间

### 🛠️ 部署步骤

#### 1. 克隆项目仓库

```bash
# 克隆CyberSecurity-Bench项目到本地
git clone https://github.com/LLM-hunter/CyberSecurity-Bench.git
```

#### 2. 创建虚拟环境

```bash
# 使用 Conda 创建环境 (推荐)
conda create --name CSBench python=3.10 -y
conda activate CSBench

# 或使用 virtualenv
python -m venv CSBench
source CSBench/bin/activate  # Linux/macOS
# CSBench\Scripts\activate   # Windows
```

#### 3. 安装 OpenCompass 评测框架

```bash
# 克隆 OpenCompass 官方仓库
git clone https://github.com/open-compass/opencompass.git
cd opencompass

# 安装核心依赖
pip install -e .

# 安装扩展功能 (根据需要选择)
pip install -e ".[api]"      # API 模型支持
pip install -e ".[lmdeploy]" # LMDeploy 推理后端
pip install -e ".[vllm]"     # vLLM 推理后端
```

#### 4. 下载 OpenCompass 数据集

```bash
# 下载核心数据集包
wget https://github.com/open-compass/opencompass/releases/download/0.2.2.rc1/OpenCompassData-core-20240207.zip

# 解压核心数据集包
unzip OpenCompassData-core-20240207.zip
```

#### 5. 配置 CyberSecurity-Bench 集成

```bash
# 回到项目根目录
cd ..

# 创建模型配置目录
mkdir -p opencompass/opencompass/configs/models/clouditera


# 复制配置文件到 OpenCompass
cp -r CyberSecurity-Bench/models/configs/api_models/* opencompass/opencompass/configs/models/clouditera/
cp -r CyberSecurity-Bench/models/configs/local_models/* opencompass/opencompass/configs/models/clouditera/

# 复制数据集文件
cp -r CyberSecurity-Bench/data/* opencompass/data/

# 复制评测配置文件到OpenCompass数据配置目录
cp -r CyberSecurity-Bench/evaluation/* opencompass/opencompass/configs/datasets/

# 复制工具脚本
cp -r CyberSecurity-Bench/tools/* opencompass/tools/
```

### ⚙️ 模型配置

#### API模型配置示例

编辑 `opencompass/opencompass/configs/models/clouditera/SecGPT_7B.py`:

```python
"""SecGPT-7B 模型配置文件

使用前请修改以下配置：
1. internlm_url: 替换为您的 API 服务地址
2. api_key: 替换为您的 API 密钥
3. 根据您的服务性能调整 query_per_second 和 batch_size
"""

import os
from opencompass.models import OpenAISDK

# 🔧 配置区域 - 请根据您的环境修改
internlm_url = 'http://your-api-server:port/v1'  # 替换为您的 API 地址
api_key = '0'  # 替换为您的 API Key

models = [
    dict(
        abbr='SecGPT-7B',               # 模型简称
        type=OpenAISDK,                 # 使用 OpenAI SDK
        path='SecGPT-7B',               # 请求服务时的模型名称
        key=api_key,                    # API 密钥
        openai_api_base=internlm_url,   # 服务地址
        rpm_verbose=True,               # 显示请求速率
        query_per_second=6,             # 请求频率限制
        max_out_len=2048,              # 最大输出长度
        max_seq_len=2048,              # 最大输入长度
        temperature=0.01,               # 生成温度
        batch_size=15,                 # 批处理大小
        retry=3,                       # 重试次数
    )
]
```

#### 本地模型配置示例

编辑 `opencompass/opencompass/configs/models/clouditera/Foundation-Sec-8B.py`:

```python
"""
Foundation-Sec-8B 本地模型配置文件

本配置文件用于在OpenCompass框架中部署Foundation-Sec-8B模型进行本地推理评测。

使用前请修改以下配置：
1. path: 替换为您的模型本地路径
2. run_cfg: 根据您的GPU配置调整GPU数量
3. engine_config: 根据您的硬件性能调整批处理大小和会话长度
4. gen_config: 根据评测需求调整生成参数

"""
from opencompass.models import TurboMindModel

models = [
    dict(
        type=TurboMindModel,
        abbr='Foundation-Sec-8B',
        path='/path/to/your/Foundation-Sec-8B/',  # 🔧 替换为您的模型路径
        engine_config=dict(session_len=16384, max_batch_size=16, tp=1),
        gen_config=dict(top_k=1, temperature=1e-6, top_p=0.9, max_new_tokens=4096),
        max_seq_len=16384,
        max_out_len=4096,
        batch_size=16,
        run_cfg=dict(num_gpus=1),  # 🔧 根据您的GPU数量调整
    )
]
```

## 🧪 评测框架

### 🔄 标准化评测流程

CyberSecurity-Bench 提供完整的评测流水线，从数据集选择到结果分析的全自动化处理：

1. **📂 选择知识库**: 从安全专业知识库中选择评测维度
2. **⚙️ 配置评测参数**: 设置模型参数、评测指标和输出格式
3. **🤖 选择评测模型**: 配置待评测的AI模型接口
4. **▶️ 运行评测脚本**: 执行标准化评测流程
5. **📊 生成分析报告**: 自动生成详细的评测报告
6. **💾 结果对比存储**: 保存结果并支持历史对比

> ⚠️ **重要提示**: 在评测前，请确保已按照[部署步骤](#🛠️-部署步骤)完成配置文件部署，并激活相应的conda环境

### 📋 评测示例

#### 🔒 安全专业知识库评测

##### 1. 网络安全综合能力评测 (CS-Eval)

> 📝 **特别说明**: CS-Eval数据集没有提供参考答案，需要先获取模型预测结果，然后前往CS-Eval官网提交获取最终评分。本项目利用大模型对预测结果进行自动答案提取。请注意，不同模型的提取效果可能存在差异，通常模型能力越强，提取结果越精准，最终得分也越可靠。

**第一步：生成模型预测结果**

```bash
# 进入OpenCompass目录
cd opencompass

# 激活环境
conda activate CSBench

# 运行CS-Eval评测 (API模型示例)
opencompass \
    --models SecGPT_7B \
    --custom-dataset-path /root/opencompass/data/cseval/cs-eval-questions.jsonl \
    --custom-dataset-data-type qa \
    --custom-dataset-infer-method gen \
    -w results/SecGPT-7B \
    --debug

# 本地模型评测示例 (指定GPU)
CUDA_VISIBLE_DEVICES=0,1 opencompass \
    --models Foundation_Sec_8B \
    --custom-dataset-path /root/opencompass/data/cseval/cs-eval-questions.jsonl \
    --custom-dataset-data-type qa \
    --custom-dataset-infer-method gen \
    -w results/Foundation-Sec-8B \
    --debug
```

**第二步：提取预测结果**
> ⚠️ **提取前配置**: 在提取模型结果前，请先修改 `opencompass/tools/process_cseval_predictions.py` 文件中的提取模型API配置。

```bash
# 使用大模型提取模型预测答案
python tools/process_cseval_predictions.py input_file_name output_file_name
```

**第三步：提交评测**

前往 [CS-Eval官网](https://cs-eval.com/#/app/submission) 提交经过模型提取答案后的Json文件获取最终评分。


##### 2. 安全认证评测 (CISSP)

> ⚠️ **评测前配置**: 在运行CISSP评测前，请先修改 `opencompass/opencompass/configs/datasets/cissp/cissp_judge.py` 文件中的judge模型API配置。

```python
# 修改文件: opencompass/opencompass/configs/datasets/cissp/cissp_judge.py
judge_model = dict(
    abbr='your_model_name',               # 修改为您的模型名称
    type=OpenAISDK,
    path='your_model_name',               # 修改为您的模型名称
    key='your_api_key',                   # 修改为您的API密钥
    openai_api_base='http://your_model_api_url:port',  # 修改为您的API地址
    # ... 其他配置保持不变
)
```

**API模型评测:**
```bash
opencompass \
    --models SecGPT_7B \
    --datasets cissp_judge \
    --max-num-workers 8 \
    -w results/SecGPT-7B \
    --debug
```

**本地模型评测:**
```bash
CUDA_VISIBLE_DEVICES=0,1 opencompass \
    --models Foundation_Sec_8B \
    --datasets cissp_judge \
    --max-num-workers 8 \
    -w results/Foundation-Sec-8B \
    --debug
```

##### 3. 威胁情报分析 (CTI-MCQ)

> ⚠️ **评测前配置**: 在运行CTI-MCQ评测前，请先修改 `opencompass/opencompass/configs/datasets/cisco/cti_mcq_judge.py` 文件中的judge模型API配置。

```python
# 修改文件: opencompass/opencompass/configs/datasets/cisco/cti_mcq_judge.py
judge_model = dict(
    abbr='your_model_name',               # 修改为您的模型名称
    type=OpenAISDK,
    path='your_model_name',               # 修改为您的模型名称
    key='your_api_key',                   # 修改为您的API密钥
    openai_api_base='http://your_model_api_url:port',  # 修改为您的API地址
    # ... 其他配置保持不变
)
```

**API模型评测:**
```bash
opencompass \
    --models SecGPT_7B \
    --datasets cti_mcq_judge \
    --max-num-workers 8 \
    -w results/SecGPT-7B \
    --debug
```

**本地模型评测:**
```bash
CUDA_VISIBLE_DEVICES=0,1 opencompass \
    --models Foundation_Sec_8B \
    --datasets cti_mcq_judge \
    --max-num-workers 8 \
    -w results/Foundation-Sec-8B \
    --debug
```

##### 4. 威胁响应案例 (CTI-RCM)

> ⚠️ **评测前配置**: 在运行CTI-RCM评测前，请先修改 `opencompass/opencompass/configs/datasets/cisco/cti_rcm_judge.py` 文件中的judge模型API配置。

```python
# 修改文件: opencompass/opencompass/configs/datasets/cisco/cti_rcm_judge.py
judge_model = dict(
    abbr='your_model_name',               # 修改为您的模型名称
    type=OpenAISDK,
    path='your_model_name',               # 修改为您的模型名称
    key='your_api_key',                   # 修改为您的API密钥
    openai_api_base='http://your_model_api_url:port',  # 修改为您的API地址
    # ... 其他配置保持不变
)
```

**API模型评测:**
```bash
opencompass \
    --models SecGPT_7B \
    --datasets cti_rcm_judge \
    --max-num-workers 8 \
    -w results/SecGPT-7B \
    --debug
```

**本地模型评测:**
```bash
CUDA_VISIBLE_DEVICES=0,1 opencompass \
    --models Foundation_Sec_8B \
    --datasets cti_rcm_judge \
    --max-num-workers 8 \
    -w results/Foundation-Sec-8B \
    --debug
```

#### 🌐 通用能力基准评测

##### 1. 数学推理能力 (GSM8K)

**API模型评测:**
```bash
opencompass \
    --models SecGPT_7B \
    --datasets gsm8k_gen \
    --max-num-workers 8 \
    -w results/SecGPT-7B \
    --debug
```

**本地模型评测:**
```bash
CUDA_VISIBLE_DEVICES=0,1 opencompass \
    --models Foundation_Sec_8B \
    --datasets gsm8k_gen \
    --max-num-workers 8 \
    -w results/Foundation-Sec-8B \
    --debug
```

##### 2. 多领域知识 (MMLU)

**API模型评测:**
```bash
opencompass \
    --models SecGPT_7B \
    --datasets mmlu_gen \
    --max-num-workers 8 \
    -w results/SecGPT-7B \
    --debug
```

**本地模型评测:**
```bash
CUDA_VISIBLE_DEVICES=0,1 opencompass \
    --models Foundation_Sec_8B \
    --datasets mmlu_gen \
    --max-num-workers 8 \
    -w results/Foundation-Sec-8B \
    --debug
```

##### 3. 复杂推理 (BBH)

**API模型评测:**
```bash
opencompass \
    --models SecGPT_7B \
    --datasets bbh_gen \
    --max-num-workers 8 \
    -w results/SecGPT-7B \
    --debug
```

**本地模型评测:**
```bash
CUDA_VISIBLE_DEVICES=0,1 opencompass \
    --models Foundation_Sec_8B \
    --datasets bbh_gen \
    --max-num-workers 8 \
    -w results/Foundation-Sec-8B \
    --debug
```

##### 4. 中文理解 (C-Eval)

**API模型评测:**
```bash
opencompass \
    --models SecGPT_7B \
    --datasets ceval_gen \
    --max-num-workers 8 \
    -w results/SecGPT-7B \
    --debug
```

**本地模型评测:**
```bash
CUDA_VISIBLE_DEVICES=0,1 opencompass \
    --models Foundation_Sec_8B \
    --datasets ceval_gen \
    --max-num-workers 8 \
    -w results/Foundation-Sec-8B \
    --debug
```


## 📊 结果展示

### 📁 结果文件结构

评测完成后，结果将保存在 `results/` 目录下（以CISSP数据集为例）：

```bash
results/cissp/
├── Foundation-Sec-8B/
│   ├── prediction/
│   │   └── foundation_sec_8b_cissp.json     # 模型预测结果
│   └── summary/
│       └── foundation_sec_8b_cissp.csv      # 评测结果汇总
└── SecGPT-7B/
    ├── prediction/
    │   └── secgpt_7b_cissp.json             # 模型预测结果
    └── summary/
        └── secgpt_7b_cissp.csv              # 评测结果汇总
```

### 📊 模型性能对比

以下是Foundation-Sec-8B模型和SecGPT-7B模型在各个数据集上的评测结果对比：

| 模型 | CS-Eval | CISSP | BBH | C-Eval | GSM8K | MMLU | CTI-MCQ | CTI-RCM |
|------|---------|-------|-----|--------|-------|------|---------|---------|
| **Foundation-Sec-8B** | 55.02 | 49.12 | 58.72 | 42.70 | 54.73 | 47.36 | 43.40 | 67.30 |
| **SecGPT-7B** | 88.24 | 77.86 | 61.51 | 70.40 | 82.94 | 70.94 | 74.56 | 70.30 |

> 📋 **评测说明**: 以上所有评测得分均使用本项目提供的评测脚本和 OpenCompass 官方评测框架运行得出，确保结果的一致性和可重现性。

### 📝 典型案例分析

以下是从各个数据集中选取的典型案例，展示了两个模型在不同安全场景下的表现对比：

#### 🔍 案例一：CISSP 数据集

**📋 输入提示词 (题目ID: 2403)**
```
Wi-Fi Protected Access 2 (WPA2) is a security protocol designed with which of the following security feature?
A. Encryption control
B. Malware attack protection
C. Data availability
D. Replay attack protection
请你只回答正确答案选项，不要额外的文字描述。
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `A` ✅ | **正确** |
| **Foundation-Sec-8B** | `A.\nB.\nC.\nD.` ❌ | **错误** |
| **标准答案** | `A` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
A
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
A.
B.
C.
D.
</details>

#### 🔍 案例二：CISSP 数据集

**📋 输入提示词 (题目ID: 37)**
```
Which of the following are all elements of a disaster recovery Plan (DRP)?以下哪些要素都是灾难恢复计划(DRP)的所有要素？
A. Document the actual Location of the ORP, developing an incident notification procedure, evaluating Costs of critical components记录 ORP 的实际位置，制定突发事件通知程序，评估关键组件的成本
B. Document the actual location of the ORP, developing an incident notification procedure, establishing recovery Locations记录 ORP 的实际位置，制定突发事件通知程序，建立恢复位置
C. Maintain Proper documentation of all server logs, developing an incident notification Procedure, establishing recovery locations维护所有服务器日志的适当文档记录，开发突发事件通知过程，建立恢复位置
D. Document the actual location of the ORP, recording minutes at all ORP planning sessions, establishing recovery Locations记录 ORP 的实际位置，记录所有 ORP 计划会话的分钟数，建立恢复位置
请你只回答正确答案选项，不要额外的文字描述。
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `B` ❌ | **错误** |
| **Foundation-Sec-8B** | `B` ❌ | **错误** |
| **标准答案** | `C` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
B
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
A
B
C
D
答案：B
参考：
</details>

#### 🔍 案例三：CISSP 数据集

**📋 输入提示词 (题目ID: 3)**
```
In a financial institution, who has the responsibility for Assigning the classification to a piece of information?在金融机构中，谁负责对一条信息进行分类？
A. Chief Financial Officer (CFO)首席财务官（首席财务官）
B. Chief Information Security Officer (CISO)首席信息安全官(CISO)
C. Originator Or nominated owner of the information该信息的发起人或指定的所有者
D. Department head responsible for Ensuring the protection of the information负责确保信息保护的部门负责人
请你只回答正确答案选项，不要额外的文字描述。
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `C` ✅ | **正确** |
| **Foundation-Sec-8B** | `C` ✅ | **正确** |
| **标准答案** | `C` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
C
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
答案：C
</details>

#### 🔍 案例四：CISSP 数据集

**📋 输入提示词 (题目ID: 12)**
```
When would an organization review a Business Continuity Management (BCM) system?组织何时会审查业务连续性管理(BCM)系统？
A. When major changes occur On systems当系统上发生重大变化时
B. When personnel changes occur当人员发生变化时
C. Before and after Disaster Recovery (DR) tests在灾难恢复(DR)测试之前和之后
D. At planned Intervals按计划间隔
请你只回答正确答案选项，不要额外的文字描述。
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `AD` ❌ | **错误** |
| **Foundation-Sec-8B** | `D` ✅ | **正确** |
| **标准答案** | `D` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
AD
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
答案：D
参考：
[REF] Business Continuity Management (BCM) - Wikipedia [/REF]
[REF] Business Continuity Management (BCM) - ISO 22301 - BSI [/REF]
[REF] Business Continuity Management (BCM) - ISO 22301 - BSI - YouTube [/REF]
</details>

#### 🔍 案例五：CTI-MCQ 数据集

**📋 输入提示词 (题目ID: 2386)**
```
Which of the following best describes the weakness categorized as CWE-794?
A. The product processes data from an upstream component but fails to handle all instances of a special element before it moves downstream.
B. The product has a vulnerability due to improper handling of user authentication, leading to unauthorized access.
C. The product does not encrypt all critical data before transmission, making it vulnerable to interception.
D. The product allows unauthorized users to access administrative functionality due to improper session management.
请你只回答正确答案选项，不要额外的文字描述。
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `A` ✅ | **正确** |
| **Foundation-Sec-8B** | `Answer: D` ❌ | **错误** |
| **标准答案** | `A` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
A
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
Answer: D
</details>

#### 🔍 案例六：CTI-MCQ 数据集

**📋 输入提示词 (题目ID: 1701)**
```
During the process of threat intelligence analysis, John, a threat analyst, successfully extracted an indication of adversary's information, such as Modus operandi, tools, communication channels, and forensics evasion strategies used by adversaries. Identify the type of threat intelligence analysis is performed by John.
A. Operational threat intelligence analysis
B. Technical threat intelligence analysis
C. Strategic threat intelligence analysis
D. Tactical threat intelligence analysis
请你只回答正确答案选项，不要额外的文字描述。
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `A` ❌ | **错误** |
| **Foundation-Sec-8B** | `D` ✅ | **正确** |
| **标准答案** | `D` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
A
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
答案：D
</details>

#### 🔍 案例七：CTI-MCQ 数据集

**📋 输入提示词 (题目ID: 153)**
```
Which of the following ports does WMI use for Remote WMI over WinRM operations?
A. A) 80 for HTTP, 443 for HTTPS
B. B) 5985 for HTTP, 5986 for HTTPS
C. C) 135 for RPC, 445 for SMB
D. D) 3306 for MySQL, 5432 for PostgreSQL
请你只回答正确答案，不要额外的文字描述。
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `B` ✅ | **正确** |
| **Foundation-Sec-8B** | `B` ✅ | **正确** |
| **标准答案** | `B` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
B
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
B
</details>

#### 🔍 案例八：CTI-MCQ 数据集

**📋 输入提示词 (题目ID: 288)**
```
Which data source ID would you use to monitor the execution and arguments of mshta.exe?
A. DS0017
B. DS0022
C. DS0029
D. DS0009
请你只回答正确答案，不要额外的文字描述。
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `C` ❌ | **错误** |
| **Foundation-Sec-8B** | `A. DS0017...` ❌ | **错误** |
| **标准答案** | `D` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
C
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
A. DS0017
B. DS0022
C. DS0029
D. DS0009
</details>

#### 🔍 案例九：CTI-RCM 数据集

**📋 输入提示词 (题目ID: 981)**
```
Analyze the following CVE description and map it to the appropriate CWE. Provide a brief justification for your choice. Ensure the last line of your response contains only the CWE ID.  CVE Description: A heap-based buffer overflow was found in the __vsyslog_internal function of the glibc library. This function is called by the syslog and vsyslog functions. This issue occurs when the openlog function was not called, or called with the ident argument set to NULL, and the program name (the basename of argv[0]) is bigger than 1024 bytes, resulting in an application crash or local privilege escalation. This issue affects glibc 2.36 and newer. 
Remember to put your final answer within \boxed{}.
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `CWE-787` ✅ | **正确** |
| **Foundation-Sec-8B** | `CWE-122` ❌ | **错误** |
| **标准答案** | `CWE-787` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
The vulnerability described in the CVE is a **heap-based buffer overflow**, which falls under the **CWE-787** category. Let's break this down to understand why this mapping is appropriate.
Understanding the Vulnerability
A **buffer overflow** occurs when more data is written to a buffer (a fixed-size block of memory) than it can hold, causing the excess data to overwrite adjacent memory locations. In this case, the overflow happens on the **heap**, which is a region of memory used for dynamic memory allocation during program execution.
The specific issue arises in the `__vsyslog_internal` function of the **glibc (GNU C Library)**. This function is part of the system's logging mechanism and is called by `syslog` and `vsyslog`. The problem occurs when:
- The `openlog` function is **not called**, or
- It is called with the `ident` argument set to **NULL**, and
- The program name (obtained from `argv[0]`) is **larger than 1024 bytes**.
In such cases, the function does not properly validate the length of the program name before copying it into a fixed-size buffer on the heap. If the program name exceeds the buffer's capacity, it overflows into adjacent memory, potentially corrupting data or even allowing an attacker to execute arbitrary code.
This type of overflow can lead to **application crashes** or, in some cases, **local privilege escalation**, depending on how the overflowed memory is accessed or modified.
Why CWE-787 is the Correct Mapping
**CWE-787** is defined as:
> *"Out-of-bounds Write: The software writes data past the end, or before the beginning, of the intended buffer."*
This directly matches the scenario described in the CVE. The overflow occurs because the program writes more data into a heap-allocated buffer than it can safely hold, without proper bounds checking.
### Summary
- **Vulnerability Type**: Heap-based buffer overflow.
- **Impact**: Application crash or local privilege escalation.
- **Root Cause**: Improper validation of input size before writing to a heap-allocated buffer.
- **CWE Mapping**: CWE-787.
This is a classic example of a buffer overflow that exploits improper memory handling, making **CWE-787** the correct identifier.
CWE-787
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
CWE-122: Heap-based Buffer Overflow
Justification: The description mentions a heap-based buffer overflow in the __vsyslog_internal function of the glibc library. This aligns with CWE-122, which is about heap-based buffer overflows.
</details>

#### 🔍 案例十：CTI-RCM 数据集

**📋 输入提示词 (题目ID: 26)**
```
Analyze the following CVE description and map it to the appropriate CWE. Provide a brief justification for your choice. Ensure the last line of your response contains only the CWE ID.  CVE Description: : Relative Path Traversal vulnerability in B&R Industrial Automation Automation Studio allows Relative Path Traversal.This issue affects Automation Studio: from 4.0 through 4.12. 
Remember to put your final answer within \boxed{}.
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `CWE-24` ❌ | **错误** |
| **Foundation-Sec-8B** | `CWE-23` ❌ | **错误** |
| **标准答案** | `CWE-22` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
The vulnerability described in the CVE relates to an **unrestricted file upload** issue in the `uploadUnity` function of the `/application/index/controller/Unity.php` file in openBI versions up to 1.0.8. This means that an attacker can manipulate the `file` argument to upload files to the server without proper restrictions. Since the vulnerability allows remote exploitation and the exploit is publicly disclosed, it poses a significant security risk.
This type of vulnerability is categorized under **CWE-22**, which stands for **"Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')".** However, in this case, the more accurate mapping would typically be **CWE-434**, "Unrestricted Upload of File with Dangerous Type," or **CWE-436**, "Incorrect Restriction of Excessive Data." But since the provided correct answer is **CWE-22**, we must consider how this classification fits the context.
CWE-22 refers to vulnerabilities where software does not properly restrict the pathnames used in file operations, potentially allowing attackers to access or manipulate files outside the intended directory structure. In the context of the given CVE, while the core issue is about unrestricted file uploads, the ability to manipulate the file path (e.g., using `../` sequences) could be considered a form of path traversal, which falls under the broader category of improper pathname restriction.
Therefore, the vulnerability aligns with **CWE-22** because it involves improper handling of file paths during the upload process, which could lead to unauthorized access or execution of malicious files.
\boxed{CWE-22}
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
CWE-434: Unrestricted Upload of File with Dangerous Type
</details>

#### 🔍 案例十一：CTI-RCM 数据集

**📋 输入提示词 (题目ID: 16)**
```
Analyze the following CVE description and map it to the appropriate CWE. Provide a brief justification for your choice. Ensure the last line of your response contains only the CWE ID.  CVE Description: A vulnerability, which was classified as critical, was found in openBI up to 1.0.8. This affects the function uploadUnity of the file /application/index/controller/Unity.php. The manipulation of the argument file leads to unrestricted upload. It is possible to initiate the attack remotely. The exploit has been disclosed to the public and may be used. The associated identifier of this vulnerability is VDB-252471. 
Remember to put your final answer within \boxed{}.
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `CWE-22` ❌ | **错误** |
| **Foundation-Sec-8B** | `CWE-434` ✅ | **正确** |
| **标准答案** | `CWE-434` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
The vulnerability described in the CVE relates to an **unrestricted file upload** issue in the `uploadUnity` function of the `/application/index/controller/Unity.php` file in openBI versions up to 1.0.8. This means that an attacker can manipulate the `file` argument to upload files to the server without proper restrictions. Since the vulnerability allows remote exploitation and the exploit is publicly disclosed, it poses a significant security risk.
This type of vulnerability is categorized under **CWE-22**, which stands for **"Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')".** However, in this case, the more accurate mapping would typically be **CWE-434**, "Unrestricted Upload of File with Dangerous Type," or **CWE-436**, "Incorrect Restriction of Excessive Data." But since the provided correct answer is **CWE-22**, we must consider how this classification fits the context.
CWE-22 refers to vulnerabilities where software does not properly restrict the pathnames used in file operations, potentially allowing attackers to access or manipulate files outside the intended directory structure. In the context of the given CVE, while the core issue is about unrestricted file uploads, the ability to manipulate the file path (e.g., using `../` sequences) could be considered a form of path traversal, which falls under the broader category of improper pathname restriction.
Therefore, the vulnerability aligns with **CWE-22** because it involves improper handling of file paths during the upload process, which could lead to unauthorized access or execution of malicious files.
\boxed{CWE-22}
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
CWE-434: Unrestricted Upload of File with Dangerous Type
</details>

#### 🔍 案例十二：CTI-RCM 数据集

**📋 输入提示词 (题目ID: 25)**
```
Analyze the following CVE description and map it to the appropriate CWE. Provide a brief justification for your choice. Ensure the last line of your response contains only the CWE ID.  CVE Description: The POST SMTP WordPress plugin before 2.8.7 does not sanitise and escape the msg parameter before outputting it back in the page, leading to a Reflected Cross-Site Scripting which could be used against high privilege users such as admin. 
Remember to put your final answer within \boxed{}.
```

**🤖 模型回答对比**

| 模型 | 预测结果 | 答案正确性 |
|------|----------|------------|
| **SecGPT-7B** | `CWE-79` ✅ | **正确** |
| **Foundation-Sec-8B** | `CWE-79` ✅ | **正确** |
| **标准答案** | `CWE-79` | - |

<details>
<summary>SecGPT-7B 完整回答</summary>
The vulnerability described in the CVE is related to **Reflected Cross-Site Scripting (XSS)**, which occurs when user-supplied input is not properly sanitized or escaped before being echoed back to the user in a web page. In this case, the `POST SMTP` WordPress plugin version before 2.8.7 fails to sanitize the `msg` parameter. When an attacker injects malicious JavaScript code into this parameter, it gets reflected back to the browser of another user—such as an admin—who views the page. If the browser executes the injected script, it can lead to unauthorized actions, data theft, or other malicious behavior.
This type of vulnerability falls under **CWE-79**, which is defined as **Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')**. This weakness occurs when software does not properly neutralize or sanitize user input that is included in a web page without proper validation or escaping, allowing attackers to execute arbitrary scripts in the context of the victim's session.
In summary, the vulnerability in the `POST SMTP` plugin is a classic example of **CWE-79** due to the lack of input sanitization and the resulting XSS risk.
\boxed{CWE-79}
</details>

<details>
<summary>Foundation-Sec-8B 完整回答</summary>
CWE-79: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
</details>
## 🐛 常见问题

### ❓ 安装问题

**Q: 安装过程中出现依赖冲突怎么办？**

A: 建议使用独立的虚拟环境，并按顺序安装依赖：
```bash
conda create --name CSBench python=3.10 -y
conda activate CSBench
cd opencompass && pip install -e .
```

**Q: 下载数据集失败怎么解决？**

A: 尝试使用国内镜像源或手动下载：
```bash
# 使用ModelScope镜像
pip install modelscope
export DATASET_SOURCE=ModelScope

# 或者手动下载数据集
wget -c https://github.com/open-compass/opencompass/releases/download/0.2.2.rc1/OpenCompassData-core-20240207.zip
```

### 🔧 配置问题

**Q: API模型连接失败怎么办？**

A: 请检查以下配置项：
- ✅ API地址格式正确 (`http://host:port/v1`)
- ✅ API Key有效且有权限
- ✅ 网络连接正常，防火墙允许访问
- ✅ 模型服务正在运行并可正常响应

**Q: 本地模型加载失败怎么办？**

A: 请检查以下配置：
```python
# 确认模型路径正确
path='/correct/path/to/your/model/',

# 确认GPU配置合理
run_cfg=dict(num_gpus=1),  # 根据实际GPU数量调整

# 确认内存配置足够
engine_config=dict(session_len=16384, max_batch_size=16, tp=1),
```


**Q: 评测结果异常怎么分析？**

A: 检查以下方面：
- 📋 查看 `work_dir/logs/` 目录下相应的日志文件了解详细错误信息
- 🔍 检查 `work_dir/predictions/` 目录下的预测结果格式
- ⚙️ 验证模型配置参数是否合理
- 📊 确认数据集路径和格式正确性


## 🙏 致谢

感谢以下项目和团队的支持：
- [SecGPT](https://github.com/Clouditera/SecGPT) - 全球首个网络安全开源大模型
- [OpenCompass](https://github.com/open-compass/opencompass) - 强大的大模型评测框架
- [OpenAI](https://openai.com/) - API标准设计参考
- [HuggingFace](https://huggingface.co/) - 模型生态支持
- 安全社区的专家们 - 提供专业知识库内容和宝贵建议
---

<div align="center">
如果这个项目对您有帮助，请给我们一个 ⭐ Star!
</div>
