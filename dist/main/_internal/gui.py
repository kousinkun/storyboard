import computation
import initialization
import c_rows_columns
import input_file
import output_result
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import input_file
import pandas as pd
import tkinter.font as font
import meassage


#最初画面
class GUI:
    def __init__(self, callback):
        self.mainroot = tk.Tk()           #创立窗口
        self.mainroot.title('storyboardツール')  #窗口名称
        self.mainroot.geometry("500x300+630+80")   #窗口的大小
        self.file_path = None
        self.savefile_path = None
        self.callback = callback
        self.pdata = None
    def interface(self):
        """"界面编写位置"""

        #文本显示
        self.Label0 = tk.Label(
            self.mainroot,
            text='LOG時間計算',
            font=("Arial", 16, "bold"),      #字体
        )
        self.Label0.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)     #sticky="nsew"：使标签的内容在单元格内居中。

                                                                                          #padx=10, pady=10：在标签四周添加一些内边距，避免文本紧贴边缘。
        #按钮显示
        # ファイルを選択イベント
        self.Button0 = tk.Button(self.mainroot, text='利用', command=self.Button0_result)
        self.Button0.grid(row=3, column=1, padx=10, pady=10)   # 使用 grid 布局
        # exe終了イベント
        self.Button1 = tk.Button(self.mainroot, text='終了', command=self.stop_program)
        self.Button1.grid(row=6, column=1, padx=10, pady=10)  # 按钮2的 grid 布局
        # 処理イベント
        self.Button2 = tk.Button(self.mainroot, text='処理', command=self.Button2_result)
        self.Button2.grid(row=4, column=1, padx=10, pady=10)  # 布局
        #保存イベント
        self.Button3 = tk.Button(self.mainroot, text='保存', command=self.Button3_result)
        self.Button3.grid(row=5, column=1, padx=10, pady=10)  # 布局
        # 设置列和行的权重，使得标签可以居中
        self.mainroot.grid_columnconfigure(0, weight=1)
        self.mainroot.grid_columnconfigure(1, weight=1)
        self.mainroot.grid_columnconfigure(2, weight=1)                                   #权重的设置，把整个画面分为n份整个n就是你这是了几个columnconfigure
                                                                                          #最终位置的决定是你按钮的设置的行列，占的几列，权重 3个因素决定的
                                                                                        #比如上部分，权重都为1所以均分，columspan占3个格子等于占满，nsew为居中。
    def Button0_result(self):
        # 当按钮点击时，调用外部文件选择函数
        self.file_path = select_file()
        if self.file_path:
            pass
        else:
            meassage.error_file(meassage.Error.csv_file)

    #处理函数
    def Button2_result(self):
        if self.file_path is None or self.file_path == '':
            meassage.error_file(meassage.Error.csv_null)
        else:
            self.pdata = self.callback(self.file_path)
            if self.pdata is None:
                # 如果回调函数返回 None，说明处理失败，不显示成功窗口
                return
            if not self.pdata.empty:
                meassage.success_root(meassage.Success.process_success)
    #保存関数
    def Button3_result(self):
        if self.file_path and self.pdata is not None and not self.pdata.empty:
            self.savefile_path = save_flie()
            if self.savefile_path:
                # 使用路径保存数据
                output_result.output_excel(self.savefile_path, self.pdata)
                # 成功之后弹出成功窗口
                meassage.success_root(meassage.Success.save_success)
                # 清空文件路径和数据
                self.file_path = None
                self.pdata = None
            else:
                meassage.error_file(meassage.Error.save_path)
        else:
            # 有文件路径但是没有数据
            if self.file_path:
                meassage.error_file(meassage.Error.process_data)
            # 没有文件路径和数据
            else:
                meassage.error_file(meassage.Error.csv_null)

    def stop_program(self):
        self.mainroot.quit()

#処理イベント
def process_data(file_path):
    # 读取excel文件
    if not file_path or file_path == '':
        # 如果文件路径为空或无效，直接返回，不继续处理
        meassage.error_file(meassage.Error.csv_null)
        return None  # 返回 None 表示处理失败
    # 如果路径有效，读取文件
    pdata = input_file.read_csv(file_path)
    # 列名を作る插入一个行
    initialization.header(pdata)

    # 初期化
    initialization.initialization(pdata)

    # 新しい列を割り込み
    if 'dec_data' not in pdata.columns:
        c_rows_columns.changecolumn(pdata, 3, 'dec_data')
    # 格差
    computation.decrease(pdata)
    print(pdata.columns)
    print(pdata['data'].dtype)
    return pdata

#ファイルを選択イベント
def select_file():
    # Tkinterのルートウィンドウを非表示にする
    root = tk.Tk()
    root.withdraw()  # 隐藏Tkinter的根窗口
    # ファイル選択ダイアログを表示
    file_path = filedialog.askopenfilename(
        title="ファイルを選択してください",  # 对话框的标题
        filetypes=[
            ("テキストファイル", "*.txt"),  # 只显示txt文件
            ("すべてのファイル", "*.*")  # 显示所有文件
        ]
    )

    return file_path


#ファイルを保存イベント
def save_flie():
    saveroot = tk.Tk()
    saveroot.withdraw()
    file_path = asksaveasfilename(
    title ="ファイルを保存するパスとファイル名を選択します。",    #如果用户没有选择文件，则返回空字符串 ""
    defaultextension =".xlsx",  # 默认文件扩展名
    filetypes=[
        ("エクセルファイル", "*.xlsx"),  # 只显示txt文件
        ("すべてのファイル", "*.*")  # 显示所有文件
    ],
    initialdir ="C:/",          # 默认的打开路径
    initialfile ="myfile.xlsx",  # 默认文件名)
    )
    if file_path:  # 如果用户选择了文件
        print(f"保存されます。: {file_path}")
    else:
        print("選択されたファイルがありません。")

    return file_path


if __name__ == '__main__':
    meassage.error_file(meassage.Error.csv_file)
    #a = GUI()
    #a.interface()
    #a.mainroot.mainloop()
















