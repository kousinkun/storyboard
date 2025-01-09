import computation
import os
import openpyxl
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
            #成功的话让背景变成绿色
            self.Button0.config(bg="green")
            # 清空前面的背景颜色
            initialization.clear_button_background(self.Button2)
            pass
        else:
            meassage.error_file(meassage.Error.csv_file)
            # 清空前面的背景颜色
            initialization.clear_button_background(self.Button0, self.Button2)

    #处理函数
    def Button2_result(self):
        if self.file_path is None or self.file_path == '':
            meassage.error_file(meassage.Error.csv_null)
        else:
            self.pdata = self.callback(self.file_path)

            if self.pdata == meassage.Error.process_data_null:           #process_data_null
                # 如果回调函数返回 None，说明处理失败，不显示成功窗口
                meassage.error_file(meassage.Error.process_data_null)
                return
            if self.pdata == meassage.Error.process_data_formula:          #process_data_formula
                meassage.error_file(meassage.Error.process_data_formula)
                return

            if not self.pdata.empty:
                # 成功的话让背景变成绿色
                self.Button2.config(bg="green")
                meassage.success_root(meassage.Success.process_success)
    #保存関数
    def Button3_result(self):
        if self.file_path and self.pdata is not None and not self.pdata.empty:
            self.savefile_path = save_flie(self.file_path)
            if self.savefile_path:
                # 使用路径保存数据
                output_result.output_excel(self.savefile_path, self.pdata)
                # 成功之后弹出成功窗口
                meassage.success_root(meassage.Success.save_success)
                # 清空文件路径和数据
                self.file_path = None
                self.pdata = None
                #清空前面的背景颜色
                initialization.clear_button_background(self.Button0, self.Button2)

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
def save_flie(file_path):
    saveroot = tk.Tk()
    saveroot.withdraw()  # 隐藏主窗口
    # 提取文件的目录路径
    directory = os.path.dirname(file_path)
    # 提取文件的文件名（不包括扩展名）
    file_name_without_extension = os.path.splitext(os.path.basename(file_path))[0]
    # 打开保存文件对话框
    file_path = asksaveasfilename(
        title="ファイルを保存するパスとファイル名を選択します。",
        defaultextension=".xlsx",
        filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")],
        initialdir=directory,  # 设置初始目录
        initialfile=file_name_without_extension, # 设置初始文件名，不带扩展名
    )

    if file_path:  # 如果用户选择了文件
        print(f"保存されます。: {file_path}")

        # 调试：打印文件保存路径
        print(f"File path selected: {file_path}")

        # 创建一个示例 DataFrame    pandas 会创建一个空白文件，但是里面没有任何数据。即便它创建了文件，文件内容可能就是空的。
        data = {
            'Column1': [1, 2, 3],
            'Column2': ['A', 'B', 'C'],
            'Column3': [4.5, 6.7, 8.9],
            'Column4': [4.5, 6.7, 8.9],
            'Column5': [4.5, 6.7, 8.9]
        }
        df = pd.DataFrame(data)

        try:
            # 调试：检查文件路径是否有效    如果文件已经存在且路径有效，to_excel() 会尝试将数据写入现有的 Excel 文件。如果路径正确，文件已经存在，并且您传入了正确的 DataFrame，则文件将包含您写入的数据。
            if not os.path.exists(os.path.dirname(file_path)):    #在没有创建 Excel 文件的情况下直接写入，有可能会遇到文件访问权限或路径不存在的问题。
                print("Error: Invalid directory path.")             #通过事先创建文件，确保路径和文件都正确，避免后续的路径错误或权限问题。
            else:
                df.to_excel(file_path, index=False)
                print(f"Excel file saved successfully: {file_path}")

        except Exception as e:
            print(f"Error while saving the file: {e}")
    else:
        print("No file selected.")

    return file_path

#処理イベント
def process_data(file_path):
    # 读取excel文件
    if not file_path or file_path == '':
        # 如果文件路径为空或无效，直接返回，不继续处理
        meassage.error_file(meassage.Error.csv_null)
        return None  # 返回 None 表示处理失败

    # 初期化
    pdata = initialization.initialization(file_path)
    print(pdata)

    return pdata


if __name__ == '__main__':
    # 文件路径

    file_path = r'C:\Users\Hongchenjun\Desktop\放送タブ移動x3_放送スクロールx3(GR_LOG_EDIAG2).xlsx'
    wb = openpyxl.load_workbook(file_path)
    #pdata = pd.read_csv(file_path, names=['og_data'], on_bad_lines='warn')
    for sheet in wb.worksheets:  # 遍历每个工作表
        for row in sheet.iter_rows():  # 遍历每一行
            for cell in row:  # 遍历每一单元格
                if isinstance(cell.value, str) and cell.value.startswith('='):
                    try:
                        # 尝试解析公式，如果发生错误说明公式无效
                        # 这里只是简单地用 eval 来检查，如果不想执行公式可以改用其他检查方法
                        eval(cell.value[1:])
                    except Exception as e:
                        # 如果公式无效，则记录并清除公式
                        print(f"无效公式: {cell.coordinate} -> {cell.value}")


    print("123456")




















