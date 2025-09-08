# Shoken Automation Project

生徒一人ひとりのよかったところを GPT で自動生成し、Excel ファイルに書き込む Python ツールです。

## 概要

Excel に記載された生徒情報（学年、出席番号、よかったところ等）を元に、OpenAI の API を使って個別コメントを自動生成します。

## フォルダ構成

shoken-automation-project/
├── main.py # 実行ファイル
├── domain/
│ └── student_record.py # Record ドメインモデル
├── service/
│ └── comment_service.py # コメント生成処理
├── util/
│ └── prompt_builder.py # プロンプト構築
├── infra/
│ └── excel_io.py # Excel 読み書き処理
├── config.py # 設定ファイル
├── test/
│ └──
├── .env # 環境変数の設定（gitignore ではじいています。）
├── .env.example # .env のサンプルです。
├── .gitignore
└── README.md # このファイル

## 必要環境

- Python 3.10 以上
- openai >=1.0.0
- openpyxl

## Excel フォーマット

- ブック名：students.xlsx
- シート名：input #今後変えます
- A 列：学年（一文目が変化します）
- B 列：クラス(システム的には使いません)
- C 列：出席番号(API に名前を投げたくないので。)
- D,E,F 列：よかったところなど。所属委員会や部活動などを入れてもいいです。皮肉はききません。
- G 列：所見が書き出されます。

## 環境変数の設定

プロジェクトルートに `.env` を作成し、以下を設定してください。
`.env.example` を参考にしてください。

## その他

- API 使用料にはご注意を

## 作者

わたし

## アイデア

内田大先生

## 協力

ChatGPT
