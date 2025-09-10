import pytest
from service.comment_service import generate_comment

# monkeypatchは一時的に処理をすり替える。たたいた時の戻り値を設定する感じ。
def test_generate_comment_returns_string(monkeypatch):
    # ダミーのレスポンス
    class DummyMessage:
        content = "テスト所見"

    class DummyChoice:
        message = DummyMessage()

    class DummyResponse:
        choices = [DummyChoice()]

    class DummyClient:
        def chat(self): return self
        def completions(self): return self
        def create(self, **kwargs): return DummyResponse()

    # clientをダミーに置き換える
    monkeypatch.setattr("service.comment_service.client", DummyClient())

    # 実際にテスト
    prompt = "明るく元気"
    result = generate_comment(prompt)
    assert isinstance(result, str)
    assert "所見" in result

def test_generate_comment_failure(monkeypatch):
    class DummyClient:
        def chat(self): return self
        def completions(self): return self
        def create(self, **kwargs): raise Exception("APIエラー")

    monkeypatch.setattr("service.comment_service.client", DummyClient())

    result = generate_comment("元気")
    assert result == "コメントの生成に失敗しました。"