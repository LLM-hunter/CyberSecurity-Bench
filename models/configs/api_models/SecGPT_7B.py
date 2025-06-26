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