# from dotenv import load_dotenv
# from openai import OpenAI,OpenAIError
from config import client, resolve_model, settings
import os

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_comment(prompt: str, mode:str = "smart") -> str:
    model_name = resolve_model(mode)
    try:
        response = client.chat.completions.create(
            model = model_name,
            messages=[
                {"role": "system", "content": "あなたは中学校の教師として、生徒の個性を引き出す所見文を作成します。"},
                {"role": "user", "content": prompt}
            ],
            temperature=settings.temperature,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"[DEBUG ERROR] {e!r}")
        print(f"コメントの生成に失敗しました。:{e}")
        return "コメントの生成に失敗しました。"