from dotenv import load_dotenv
from openai import OpenAI,OpenAIError
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_comment(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o",  # または "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "あなたは中学校の教師として、生徒の個性を引き出す所見文を作成します。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"コメントの生成に失敗しました:{e}")
        return "コメントの生成に失敗しました。"