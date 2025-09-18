import pytest
from service.comment_service import generate_comment

# 本テストの意義
# generate_comment が例外を投げずに動作すること 
# レスポンスから choices[0].message.content を正しく取り出して返していること
# 返却値の型が期待通り str であること

# monkeypatchは一時的に処理をすり替える。たたいた時の戻り値を設定する感じ。
def test_generate_comment_returns_string(monkeypatch):
    # ダミーのレスポンス
    # 過剰梱包に見えるが、これはOpenAI APIのレスポンスresponse.choices[0].message.contentの形に。
    class DummyMessage:
        content = "テスト所見"
    class DummyChoice:
        message = DummyMessage()
    class DummyResponse:
        choices = [DummyChoice()]
    class DummyCompletions:
        def create(self, **kwargs):
            return DummyResponse()
    class DummyChat:
        completions = DummyCompletions()

    # 実際のレスポンスの作成は
    # response = client.chat.completions.create(
    #   model...なので、
    # clientのchatは自身を、completionsも自身を返させて、createのみ、DummyResponseを返させる。
    # responseの構造は関数ではなく、ぞれぞれ入れ子関係の属性。大量に梱包されたものを開封する感じ。
    class DummyClient:
        chat = DummyChat()

    # comment_service内のclientをダミーに置き換える
    monkeypatch.setattr("service.comment_service.client", DummyClient())

    # 実際にテスト
    prompt = "明るく元気"
    result = generate_comment(prompt)
    print("DEBUG:", result)
    assert isinstance(result, str)  # resultの型がstrかどうかのチェック
    assert "所見" in result         # resultに"所見"がふくまれているかチェック 

def test_generate_comment_failure(monkeypatch):
    # createが発動した瞬間例外処理に入るため、Responseすら不要
    class DummyClient:
        def chat(self): return self
        def completions(self): return self
        def create(self, **kwargs): raise Exception("APIエラー")

    monkeypatch.setattr("service.comment_service.client", DummyClient())

    result = generate_comment("元気")
    assert result == "コメントの生成に失敗しました。"