from opencompass.openicl.icl_prompt_template import PromptTemplate
from opencompass.openicl.icl_retriever import ZeroRetriever
from opencompass.openicl.icl_inferencer import GenInferencer
from opencompass.evaluator import GenericLLMEvaluator
from opencompass.datasets import generic_llmjudge_postprocess, CustomDataset
from opencompass.models import OpenAISDK

# Judge model configuration
judge_model = dict(
    abbr='your_model_name',
    type=OpenAISDK,
    path='your_model_name',
    key='0',
    openai_api_base='http://your_model_api_url:port',  # 请根据您的judge模型API地址修改
    rpm_verbose=True,
    query_per_second=2,
    max_out_len=2048,
    max_seq_len=8192,
    temperature=0.01,
    batch_size=4,
    retry=3,
)

# Dataset reader configuration
cissp_reader_cfg = dict(input_columns=['question', 'A', 'B', 'C', 'D'], output_column='answer')

# Inference configuration
cissp_infer_cfg = dict(
    prompt_template=dict(
        type=PromptTemplate,
        template=dict(
            round=[
                dict(
                    role='HUMAN',
                    prompt='{question}\nA. {A}\nB. {B}\nC. {C}\nD. {D}\n请你只回答正确答案选项，不要额外的文字描述。',
                ),
            ]
        ),
    ),
    retriever=dict(type=ZeroRetriever),
    inferencer=dict(type=GenInferencer),
)

# Template for the LLM judge
GRADER_TEMPLATE = """
Please as a grading expert, judge whether the final answers given by the candidates below are consistent with the standard answers, that is, whether the candidates answered correctly. 

Here are some evaluation criteria:
1. Please refer to the given standard answer. You don't need to re-generate the answer to the question because the standard answer has been given. You only need to judge whether the candidate's answer is consistent with the standard answer according to the form of the question. Don't try to answer the original question. You can assume that the standard answer is definitely correct.
2. Because the candidate's answer may be different from the standard answer in the form of expression, before making a judgment, please understand the question and the standard answer first, and then judge whether the candidate's answer is correct, but be careful not to try to answer the original question.
3. Some answers may contain multiple items, such as multiple-choice questions, multiple-select questions, fill-in-the-blank questions, etc. As long as the answer is the same as the standard answer, it is enough. For multiple-select questions and multiple-blank fill-in-the-blank questions, the candidate needs to answer all the corresponding options or blanks correctly to be considered correct.
4. Some answers may be expressed in different ways, such as some answers may be a mathematical expression, some answers may be a textual description, as long as the meaning expressed is the same. And some formulas are expressed in different ways, but they are equivalent and correct.
5. If the prediction is given with \\boxed{}, please ignore the \\boxed{} and only judge whether the candidate's answer is consistent with the standard answer.

Please judge whether the following answers are consistent with the standard answer based on the above criteria. Grade the predicted answer of this new question as one of:
A: CORRECT 
B: INCORRECT
Just return the letters "A" or "B", with no text around it.

Here is your task. Simply reply with either CORRECT, INCORRECT. Don't apologize or correct yourself if there was a mistake; we are just trying to grade the answer.

<Original Question Begin>: 
{question}
<Original Question End>

<Gold Target Begin>: 
{answer}
<Gold Target End>

<Predicted Answer Begin>: 
{prediction}
<Predicted End>

Judging the correctness of candidates' answers:
""".strip()

# Evaluation configuration using LLM as judge
cissp_eval_cfg = dict(
    evaluator=dict(
        type=GenericLLMEvaluator,
        prompt_template=dict(
            type=PromptTemplate,
            template=dict(
                begin=[
                    dict(
                        role='SYSTEM',
                        fallback_role='HUMAN',
                        prompt="You are a helpful assistant who evaluates the correctness and quality of models' outputs.",
                    )
                ],
                round=[
                    dict(role='HUMAN', prompt=GRADER_TEMPLATE),
                ],
            ),
        ),
        dataset_cfg=dict(
            type=CustomDataset,
            path='/root/opencompass/data/cissp',
            file_name='cissp.jsonl',
            reader_cfg=cissp_reader_cfg,
        ),
        judge_cfg=judge_model,
        dict_postprocessor=dict(type=generic_llmjudge_postprocess),
    ),
)

# Main dataset configuration - this will be imported by OpenCompass CLI
datasets = [
    dict(
        abbr='cissp_judge',
        type=CustomDataset,
        path='/root/opencompass/data/cissp',
        file_name='cissp.jsonl',
        reader_cfg=cissp_reader_cfg,
        infer_cfg=cissp_infer_cfg,
        eval_cfg=cissp_eval_cfg,
    )
]

# Legacy name for backward compatibility
cissp_datasets = datasets
