from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_comment(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",  # または "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "あなたは教師のように丁寧で、児童の個性を引き出す所見文を作成します。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
