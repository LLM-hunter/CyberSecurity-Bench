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
        path='/root/.xinference/models/Foundation-Sec-8B/', # 🔧 替换为您的模型路径
        engine_config=dict(session_len=16384, max_batch_size=16, tp=1),
        gen_config=dict(top_k=1, temperature=1e-6, top_p=0.9, max_new_tokens=4096),
        max_seq_len=16384,
        max_out_len=4096,
        batch_size=16,
        run_cfg=dict(num_gpus=1),
    )
]