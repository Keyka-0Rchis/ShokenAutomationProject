# 参考：https://www.shido.info/py/tkinter2.html

import sys
import tkinter
from tkinter import filedialog,Label

class MainWindow:
    def __init__(self, root, run_generate):
        # フィールド変数。ui部品は各メソッドで編集したいのでフィールド変数で宣言したほうがいい。
        self.filepath = None
        self.outer = tkinter.Frame(root, padx=30, pady=20)
        self.row1_outer = tkinter.Frame(self.outer)
        # ラベル 第一引数の入れ子になる
        self.file_select_label = tkinter.Label(self.row1_outer, text="Excelファイルを選択してください。：")
        # ボタン。commandで実行するメソッドを選択
        self.file_select_button = tkinter.Button(self.row1_outer, text="ファイルを選択", command=self.select_file)
        # ラベル、ボタンの下に、ファイルが選択されたらパスが出てくるラベルを用意
        self.selected_path_label = tkinter.Label(self.outer, text="")

        self.result_label = tkinter.Label(self.outer, text="")

        self.submit_button = tkinter.Button(self.outer, text="生成開始", command=self.run)
        self.run_generate = run_generate

    # 外周のフレーム。ウィンドウ枠との間の余白制御。
    def outer_init(self):
        self.outer.grid(row=0,column=0,sticky="nsew")

    def row1_outer_init(self):
        self.row1_outer.grid(row=0, column=0,sticky="w")

    def file_select_label_init(self):
        # pady は pad y で垂直方向のパッド。cssでいうpadding
        # label.pack(pady=10)
        # より柔軟に配置したいのでgridを採用。見た目って結構モチベに直結すると思う。
        self.file_select_label.grid(row=0, column=0, pady=5)

    def file_select_button_init(self):
        # button.pack(pady=5, anchor="w")
        self.file_select_button.grid(row=0,column=1,padx=5, pady=5)

    def selected_path_label_init(self):
        self.selected_path_label.grid(row=1, column=0, pady=5, columnspan=2)

    def select_file(self):
        # filedialogでファイル選択画面へ。なんて便利なんだろう。
        self.filepath = filedialog.askopenfilename(
            title="Excelファイルを選択してください",
            filetypes=[("Excelファイル", "*.xlsx *.xls")]
        )
        if self.filepath:
            self.selected_path_label.config(text=f"選択されたファイル:" + self.filepath)

    def result_label_init(self):
        self.result_label.grid(row=2, column=0)

    def submit_button_init(self):
        self.submit_button.grid(row=5,column=0)

    def run(self):
        success, fail = self.run_generate(self.filepath)
        if success>0 or fail>0: 
            self.result_label.config(text=f"完了しました→成功：{success}件　失敗：{fail}件")
        else:
            self.result_label.config(text=f"生成されませんでした")

# # ウィンドウを作成
# root = tkinter.Tk()
# # ウィンドウタイトルの設定
# root.title("所見自動生成ー所見綴ー")
# # ウィンドウサイズの設定。今回は動的に、、、。("1080x920")とかで設定できる
# root.geometry("600x500")

# ui = MainWindow(root)
# ui.outer_init()
# ui.row1_outer_init()
# ui.file_select_label_init()
# ui.file_select_button_init()
# ui.selected_path_label_init()
# ui.submit_button_init()

# # 最後にこれを書く。これはウィンドウの永続化。イベント発生まで表示させるための一文。
# root.mainloop()