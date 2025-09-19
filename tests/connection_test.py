from config import client, resolve_model

response = client.chat.completions.create(
    model=resolve_model("smart"),
    messages=[{"role": "user", "content": "接続テストだよ"}]
)
print(response.choices[0].message.content)
