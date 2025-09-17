# service/prompt_builder.py

def build_prompt(record):
    """
    学年・出席番号・よかったことからプロンプト文字列を構築する。
    record: StudentRecordインスタンス
    return: str（生成用のプロンプト）
    """

    # 学年であいさつを変える
    if int(record.grade) == 3:
        greeting = "卒業おめでとうございます。"     
    else:
        greeting = "進級おめでとうございます。"

    # よかったことを箇条書きに整形
    if not record.good_points:
        good_parts = "特に目立った記録はありません。"
    else:
        good_parts = "\n".join(f"- {pt}" for pt in record.good_points)

    prompt = f"""
        以下は出席番号 {record.student_id} の生徒の今年度の記録です。
        この情報をもとに、{greeting}に続けて、年度末の所見文を作成してください。

        【よかったところ】
        {good_parts}

        ・日本語の敬体（です・ます）で200〜300文字でお願いします。
        ・前向きな内容にしてください。
        ・名前は使わず、「この生徒は〜」「日々の学校生活では〜」などでOKです。
        ・よかったところをすべて記述する必要はありません。
    """

    return prompt
