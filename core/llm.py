from openai import OpenAI

SYSTEM_PROMPT = """
Você é um assistente acadêmico especializado em Saúde Ocupacional e Segurança Pública.
Tema central: desconforto musculoesquelético relacionado ao uso do fardamento operacional.
Responda com clareza e objetividade.
"""

def chat_answer(user_text: str):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ],
        temperature=0.3
    )
    return response.choices[0].message.content
