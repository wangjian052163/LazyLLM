# flake8: noqa: E501

model_name_mapping = {
    "Llama-3-8B": {"huggingface": "meta-llama/Meta-Llama-3-8B"},
    "Llama-3-70B": {"huggingface": "meta-llama/Meta-Llama-3-70B"},
    "Llama-2-7b": {"huggingface": "meta-llama/Llama-2-7b"},
    "Llama-2-13b": {"huggingface": "meta-llama/Llama-2-13b"},
    "Llama-2-70b": {"huggingface": "meta-llama/Llama-2-70b"},
    "Llama-7b": {"huggingface": "meta-llama/CodeLlama-7b-hf"},
    "Llama-13b": {"huggingface": "meta-llama/CodeLlama-13b-hf"},
    "Llama-34b": {"huggingface": "meta-llama/CodeLlama-34b-hf"},
    "Llama-70b": {"huggingface": "meta-llama/CodeLlama-70b-hf"},

    "GLM3-6B": {"huggingface": "THUDM/chatglm3-6b", "modelscope": "ZhipuAI/chatglm3-6b"},
    "GLM3-6B-32K": {"huggingface": "THUDM/chatglm3-6b-32k", "modelscope": "ZhipuAI/chatglm3-6b-32k"},
    "GLM3-6B-128K": {"huggingface": "THUDM/chatglm3-6b-128k", "modelscope": "ZhipuAI/chatglm3-6b-128k"},

    "Qwen-1.8B": {"huggingface": "Qwen/Qwen-1_8B", "modelscope": "qwen/Qwen-1_8B"},
    "Qwen-7B": {"huggingface": "Qwen/Qwen-7B", "modelscope": "qwen/Qwen-7B"},
    "Qwen-14B": {"huggingface": "Qwen/Qwen-14B", "modelscope": "qwen/Qwen-14B"},
    "Qwen-72B": {"huggingface": "Qwen/Qwen-72B", "modelscope": "qwen/Qwen-72B"},
    "Qwen1.5-1.8B": {"huggingface": "Qwen/Qwen1.5-1.8B", "modelscope": "qwen/Qwen1.5-1.8B"},
    "Qwen1.5-4B": {"huggingface": "Qwen/Qwen1.5-4B", "modelscope": "qwen/Qwen1.5-4B"},
    "Qwen1.5-7B": {"huggingface": "Qwen/Qwen1.5-7B", "modelscope": "qwen/Qwen1.5-7B"},
    "Qwen1.5-14B": {"huggingface": "Qwen/Qwen1.5-14B", "modelscope": "qwen/Qwen1.5-14B"},
    "Qwen1.5-72B": {"huggingface": "Qwen/Qwen1.5-72B", "modelscope": "qwen/Qwen1.5-72B"},

    "internlm-20b": {"huggingface": "internlm/internlm-20b", "modelscope": "Shanghai_AI_Laboratory/internlm-20b"},
    "internlm2-1_8b": {"huggingface": "internlm/internlm2-1_8b", "modelscope": "Shanghai_AI_Laboratory/internlm2-1_8b"},
    "internlm2-20b": {"huggingface": "internlm/internlm2-20b", "modelscope": "Shanghai_AI_Laboratory/internlm2-20b"},
    "internlm2-7b": {"huggingface": "internlm/internlm2-7b", "modelscope": "Shanghai_AI_Laboratory/internlm2-7b"},
    "internlm2-chat-1_8b": {"huggingface": "internlm/internlm2-chat-1_8b", "modelscope": "Shanghai_AI_Laboratory/internlm2-chat-1_8b"},
    "internlm2-chat-1_8b-sft": {"huggingface": "internlm/internlm2-chat-1_8b-sft", "modelscope": "Shanghai_AI_Laboratory/internlm2-chat-1_8b-sft"},
    "internlm2-chat-20b": {"huggingface": "internlm/internlm2-chat-20b", "modelscope": "Shanghai_AI_Laboratory/internlm2-chat-20b"},
    "internlm2-chat-20b-4bits": {"huggingface": "internlm/internlm2-chat-20b-4bits", "modelscope": "Shanghai_AI_Laboratory/internlm2-chat-20b-4bits"},
    "internlm2-chat-20b-sft": {"huggingface": "internlm/internlm2-chat-20b-sft", "modelscope": "Shanghai_AI_Laboratory/internlm2-chat-20b-sft"},
    "internlm2-chat-7b": {"huggingface": "internlm/internlm2-chat-7b", "modelscope": "Shanghai_AI_Laboratory/internlm2-chat-7b"},
    "internlm2-chat-7b-4bits": {"huggingface": "internlm/internlm2-chat-7b-4bits", "modelscope": "Shanghai_AI_Laboratory/internlm2-chat-7b-4bits"},
    "internlm2-chat-7b-sft": {"huggingface": "internlm/internlm2-chat-7b-sft", "modelscope": "Shanghai_AI_Laboratory/internlm2-chat-7b-sft"},
    "internlm2-math-20b": {"huggingface": "internlm/internlm2-math-20b", "modelscope": "Shanghai_AI_Laboratory/internlm2-math-20b"},
    "internlm2-math-7b": {"huggingface": "internlm/internlm2-math-7b", "modelscope": "Shanghai_AI_Laboratory/internlm2-math-7b"},
    "internlm-7b": {"huggingface": "internlm/internlm-7b", "modelscope": "Shanghai_AI_Laboratory/internlm-7b"},
    "internlm-chat-20b": {"huggingface": "internlm/internlm-chat-20b", "modelscope": "Shanghai_AI_Laboratory/internlm-chat-20b"},
    "internlm-chat-20b-4bit": {"huggingface": "internlm/internlm-chat-20b-4bit", "modelscope": "Shanghai_AI_Laboratory/internlm-chat-20b-4bit"},
    "internlm-chat-7b": {"huggingface": "internlm/internlm-chat-7b", "modelscope": "Shanghai_AI_Laboratory/internlm-chat-7b"},
    "internlm-xcomposer2-4khd-7b": {"huggingface": "internlm/internlm-xcomposer2-4khd-7b", "modelscope": "Shanghai_AI_Laboratory/internlm-xcomposer2-4khd-7b"},
    "internlm-xcomposer2-7b": {"huggingface": "internlm/internlm-xcomposer2-7b", "modelscope": "Shanghai_AI_Laboratory/internlm-xcomposer2-7b"},
    "internlm-xcomposer2-7b-4bit": {"huggingface": "internlm/internlm-xcomposer2-7b-4bit", "modelscope": "Shanghai_AI_Laboratory/internlm-xcomposer2-7b-4bit"},
    "internlm-xcomposer2-vl-1_8b": {"huggingface": "internlm/internlm-xcomposer2-vl-1_8b", "modelscope": "Shanghai_AI_Laboratory/internlm-xcomposer2-vl-1_8b"},
    "internlm-xcomposer2-vl-7b": {"huggingface": "internlm/internlm-xcomposer2-vl-7b", "modelscope": "Shanghai_AI_Laboratory/internlm-xcomposer2-vl-7b"},
    "internlm-xcomposer2-vl-7b-4bit": {"huggingface": "internlm/internlm-xcomposer2-vl-7b-4bit", "modelscope": "Shanghai_AI_Laboratory/internlm-xcomposer2-vl-7b-4bit"},
    "internlm-xcomposer-7b": {"huggingface": "internlm/internlm-xcomposer-7b", "modelscope": "Shanghai_AI_Laboratory/internlm-xcomposer-7b"},
    "internlm-xcomposer-7b-4bit": {"huggingface": "internlm/internlm-xcomposer-7b-4bit", "modelscope": "Shanghai_AI_Laboratory/internlm-xcomposer-7b-4bit"},
    "internlm-xcomposer-vl-7b": {"huggingface": "internlm/internlm-xcomposer-vl-7b", "modelscope": "Shanghai_AI_Laboratory/internlm-xcomposer-vl-7b"},

    "Baichuan-13B-Chat": {"huggingface": "baichuan-inc/Baichuan-13B-Chat", "modelscope": "baichuan-inc/Baichuan-13B-Chat"},
    "Baichuan2-13B-Chat": {"huggingface": "baichuan-inc/Baichuan2-13B-Chat", "modelscope": "baichuan-inc/Baichuan2-13B-Chat"},
    "Baichuan2-13B-Chat-4bits": {"huggingface": "baichuan-inc/Baichuan2-13B-Chat-4bits", "modelscope": "baichuan-inc/Baichuan2-13B-Chat-4bits"},
    "Baichuan2-7B-Chat": {"huggingface": "baichuan-inc/Baichuan2-7B-Chat", "modelscope": "baichuan-inc/Baichuan2-7B-Chat"},
    "Baichuan2-7B-Chat-4bits": {"huggingface": "baichuan-inc/Baichuan2-7B-Chat-4bits", "modelscope": "baichuan-inc/Baichuan2-7B-Chat-4bits"},
    "Baichuan2-7B-Intermediate-Checkpoints": {"huggingface": "baichuan-inc/Baichuan2-7B-Intermediate-Checkpoints", "modelscope": "baichuan-inc/Baichuan2-7B-Intermediate-Checkpoints"},
    "baichuan-7B": {"huggingface": "baichuan-inc/Baichuan-7B", "modelscope": "baichuan-inc/baichuan-7B"},

    "bge-large-zh-v1.5": {"huggingface": "BAAI/bge-large-zh-v1.5", "modelscope": "AI-ModelScope/bge-large-zh-v1.5", "type":"embed"},
    "bge-reranker-large": {"huggingface": "BAAI/bge-reranker-large", "modelscope": "Xorbits/bge-reranker-large", "type":"embed"},
}
