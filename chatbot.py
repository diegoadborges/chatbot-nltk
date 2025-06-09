import torch
from transformers import pipeline

model_id = "meta-llama/Llama-3.2-1B-Instruct"
pipe = pipeline(
    "text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)


def get_response(user_input: str) -> str:
    messages = [
        {
            "role": "system",
            "content": (
                """Você é um suporte técnico de T.I. especializado em resolver dúvidas e problemas relacionados a tecnologia, 
                como computadores, redes, softwares, hardware, sistemas operacionais, segurança da informação e suporte técnico geral. 
                Qualquer pergunta que não esteja relacionada a suporte técnico ou tecnologia da informação, 
                você deve responder apenas com: 'Desculpe, só posso responder perguntas relacionadas a suporte técnico.'
                """
            ),
        },
        {"role": "user", "content": user_input},
    ]

    outputs = pipe(
        messages,
        max_new_tokens=4096,
    )

    return outputs[0]["generated_text"][-1]["content"]
