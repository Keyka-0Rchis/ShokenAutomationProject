# Shoken Automation Project

生徒一人ひとりのよかったところをGPTで自動生成し、Excelファイルに書き込むPythonツールです。

## 概要

Excelに記載された生徒情報（学年、出席番号、よかったところ等）を元に、OpenAIのAPIを使って個別コメントを自動生成します。

## フォルダ構成

shoken-automation-project/
├── main.py # 実行ファイル
├── domain/
│ └── student_record.py # Recordドメインモデル
├── service/
│ └── comment_service.py # コメント生成処理
├── util/
│ └── prompt_builder.py # プロンプト構築
├── infra/
│ └── excel_io.py # Excel読み書き処理
├── .env # APIキー格納（gitignoreではじいています。）
├── .gitignore
└── README.md # このファイル


## 必要環境

- Python 3.10以上
- openai >=1.0.0
- openpyxl

## Excelフォーマット
- ブック名：students.xlsx
- シート名：input #今後変えます
- A列：学年（一文目が変化します）
- B列：クラス(システム的には使いません)
- C列：出席番号(APIに名前を投げたくないので。)
- D,E,F列：よかったところなど。所属委員会や部活動などを入れてもいいです。皮肉はききません。
- G列：所見が書き出されます。

##その他
- API使用料にはご注意を

## 作者
わたし

## アイデア
内田大先生

## 協力
ChatGPT
