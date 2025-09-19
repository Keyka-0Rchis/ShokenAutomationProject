from infra.excel_io import read_records, write_comments
from util.prompt_builder import build_prompt
from service.comment_service import generate_comment
from domain.student_record import Record

def generate_control(filename, on_progress=None) -> tuple[int,int] :
    input_file = filename
    output_file = filename

    success_count = 0
    failed_count = 0

    # 1. Excelから生徒の記録を読み込む
    records = read_records(input_file)

    # 進捗バーのための最大値
    total = len(records)

    # 進捗の初期設定
    if on_progress:
        on_progress(0, total, success_count, failed_count, None)

    # 2. 各レコードからプロンプトを生成してコメントを作る
    for idx, record in enumerate(records,start=1):
        prompt = build_prompt(record)
        try:
            comment = generate_comment(prompt)
            record.comment = comment
            success_count += 1
            print("成功")
        except Exception as e:
            comment = "※コメント生成に失敗しました"
            print(f"Error: {e}")
            failed_count += 1
            print("失敗")
        if on_progress:
            on_progress(idx, total, success_count, failed_count, record)
        

    # 3. 出力ファイルに書き出す
    write_comments(records, output_file)

    # 4. 成功した件数と失敗した件数をUIに報告する
    return (success_count,failed_count)