import pytest
from infra.excel_io import read_records, write_comments
from util.prompt_builder import build_prompt
from service import comment_service
from service.comment_service import generate_comment
from domain.student_record import Record

# ダミーExcelファイル作成のためにインポート
from openpyxl import Workbook
# ダミーExcelは永続化不要。一時ファイルで十分。
import tempfile

def test_integration_flow(monkeypatch):
    # ワークブック作成
    wb = Workbook()
    ws = wb.active
    # シート名を設定
    ws.title = "input"

    # ダミーデータ行
    ws.append([3, "A", 1, "テスト用のよかった点1"])
    ws.append([1, "B", 2, "テスト用のよかった点2", "テスト用の良かった点3"])
    ws.append([2, "A", 1])

    # APIを用いたgenerate_commentをモック
    def mock_generate_comment(prompt):
        return "本物だと思った？残念、モックでした！"
    
    # generate_commentをmonkeypatchで差し替え
    monkeypatch.setattr(comment_service, "generate_comment", mock_generate_comment)
    
    # 一時ファイルとして保存
    # tempfileはユニークな名前を自動生成。suffixは拡張子、delete=trueだと、ファイルを閉じると即削除。まずいのでfalseに。
    tmp = tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False)
    wb.save(tmp.name)

    # xlsxを開封
    records = read_records(tmp.name)

    for record in records:
        prompt = build_prompt(record)

        response = comment_service.generate_comment(prompt)

        record.comment = response  # Recordにプロパティ追加してある前提

    write_comments(records, tmp.name)

    assert "本物だと思った？" in response







