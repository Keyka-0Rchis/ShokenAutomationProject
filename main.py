import tkinter
from ui.main_window import MainWindow
from controller.generate_controller import generate_control

def main():
    # ウィンドウを作成
    root = tkinter.Tk()
    # ウィンドウタイトルの設定
    root.title("所見自動生成ー所見綴ー")
    # ウィンドウサイズの設定。
    root.geometry("600x500")

    # 若干DIっぽく
    ui = MainWindow(root,run_generate=generate_control)
    ui.outer_init()
    ui.row1_outer_init()
    ui.file_select_label_init()
    ui.file_select_button_init()
    ui.result_label_init()
    ui.selected_path_label_init()
    ui.submit_button_init()

    # 最後にこれを書く。これはウィンドウの永続化。イベント発生まで表示させるための一文。
    root.mainloop()

if __name__ == "__main__":
    main()
