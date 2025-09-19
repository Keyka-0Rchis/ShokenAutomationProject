from infra.excel_io import read_records, write_comments
from util.prompt_builder import build_prompt
from service.comment_service import generate_comment
from domain.student_record import Record

def generate_control(filename):
    input_file = filename
    output_file = filename

    # 1. Excelから生徒の記録を読み込む
    records = read_records(input_file)

    # 2. 各レコードからプロンプトを生成してコメントを作る
    for record in records:
        prompt = build_prompt(record)
        try:
            comment = generate_comment(prompt)
        except Exception as e:
            comment = "※コメント生成に失敗しました"
            print(f"Error: {e}")
        record.comment = comment  # Recordにプロパティ追加してある前提

    # 3. 出力ファイルに書き出す
    write_comments(records, output_file)