# Shoken Automation Project

生徒一人ひとりのよかったところを GPT で自動生成し、Excel ファイルに書き込む Python ツールです。

## 概要

Excel に記載された生徒情報（学年、出席番号、よかったところ等）を元に、OpenAI の API を使って個別コメントを自動生成します。

## フォルダ構成
```
shoken-automation-project/
├── main.py # 実行ファイル。uiの起動などを定義しています。
├── config.py # 設定ファイルです。ここでenvを読み取ったりします。
├── controller/
│ └── generate_controller.py # 所見生成までのロジックの流れを定義しています。
├── domain/
│ └── student_record.py # Record ドメインモデル
├── service/
│ └── comment_service.py # コメント生成処理
├── util/
│ └── prompt_builder.py # プロンプト構築
├── infra/
│ └── excel_io.py # Excel 読み書き処理
├── tests/
│ └──integration/
│   └──test_integration_flow.py # 結合テストです。ダミーのExcelファイルを作成し、読み取り、書き出しを行います。APIでのコメント生成はモックです。
│ └──unit/
│   └──test_comment_service.py # 所見生成の戻り値の方などをテストする単体テストです
│   └──test_prompt_builder.py # 所見生成のためのプロンプト作成の単体テストです
├── ui/
│ └── main_window.py # 起動時の画面をTkinterで作成しています。
├── .env # 環境変数の設定（gitignore ではじいています。）
├── .env.example # .env のサンプルです。
├── .gitignore
└── README.md # このファイル
```
## 必要環境

- Python 3.10 以上
- pip（または uv/poetry 等）
- インターネット接続（OpenAI API 利用時）

## Excel フォーマット

- ブック名：任意です
- シート名：input #今後変えます
- A 列：学年（一文目が変化します）
- B 列：クラス(システム的には使いません)
- C 列：出席番号(API に名前を投げたくないので。)
- D,E,F 列：よかったところなど。所属委員会や部活動などを入れてもいいです。皮肉はききません。
- G 列：所見が書き出されます。

## 環境変数の設定

プロジェクトルートに `.env` を作成し、以下を設定してください。

OPENAI_API_KEY=sk-xxxxx
または、OPENAI_BASE_URL=https://api.openai.com/v1（自前のプロキシなどを使う場合）

モデル/温度の上書き
OPENAI_MODEL=gpt-4o
（省略時プリセット: smart=gpt-4o, fast=gpt-4o-mini, vision=gpt-4o-mini）
OPENAI_TEMPERATURE=0.7
`.env.example` を参考にしてください。

## 使い方
コンソールにて
python main.py
1.「ファイルを選択」から Excel を選ぶ（ブック名は任意、シート名は input）。
2.「実行」を押すと生成が始まり、進捗バーが増えていきます。
3.完了後、所見が Excel に書き戻されます（既定は G 列）。

## テストについて
すべてのテスト
pytest -q

カバレッジ（任意）
pip install coverage
coverage run -m pytest
coverage report -m

