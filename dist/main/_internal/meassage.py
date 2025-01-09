import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename
import input_file
from enum import Enum
class Error(Enum):
    csv_file = 1               #选的不是csv文件
    csv_format = 2              #这个文件里面的格式不对
    csv_null = 3                #没选到file
    save_path = 4               #没有保存位置
    process_data = 5            #没有文件处理

class Success(Enum):
    process_success = 1        #処理成功
    save_success = 2           #保存成功

#エラー画面
def error_file(error_number):
    error_number = error_number
    error_root = tk.Toplevel()
    error_root.title("Error")
    error_root.geometry("300x200+630+80")
    if error_number == Error.csv_file:
        Label0 = tk.Label(
            error_root,
            text='CSVファイルを選択してください',
            font=("Arial", 10, "bold"),  # 字体
        )
        Label0.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    elif error_number == Error.csv_format:
        Label0 = tk.Label(
            error_root,
            text='ファイルのフォマードが違います！',
            font=("Arial", 10, "bold"),  # 字体
        )
        Label0.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
    elif error_number == Error.csv_null:
        Label0 = tk.Label(
            error_root,
            text='CSVファイルを選択してください!',
            font=("Arial", 10, "bold"),  # 字体
        )
        Label0.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
    elif error_number == Error.save_path:
        Label0 = tk.Label(
            error_root,
            text='保存パスが選択されていない!',
            font=("Arial", 10, "bold"),  # 字体
        )
        Label0.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
    elif error_number == Error.process_data:
        Label0 = tk.Label(
            error_root,
            text='データを処理していない!',
            font=("Arial", 10, "bold"),  # 字体
        )
        Label0.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=10, pady=10)
    else:
        print('program is error')

    Button0 = tk.Button(error_root, text='戻す', command=error_root.destroy)
    Button0.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    # 设置列和行的权重，使得标签可以居中
    error_root.grid_columnconfigure(0, weight=1)
    error_root.grid_columnconfigure(1, weight=1)
    # 设置行的权重，使得行之间均匀分布

def success_root(success_number):
    success_number = success_number
    success_root = tk.Toplevel()
    success_root.title('success')
    success_root.geometry("300x200+630+80")
    if success_number == Success.process_success:
        Label0 = tk.Label(
            success_root,
            text='処理完了しました。',
            font=("Arial", 10, "bold"),  # 字体
        )
        Label0.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    elif success_number == Success.save_success:
        Label0 = tk.Label(
            success_root,
            text='保存しました。',
            font=("Arial", 10, "bold"),  # 字体
        )
        Label0.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
    else:
        print('program is error')
    Button0 = tk.Button(success_root, text='確認', command=success_root.destroy)
    Button0.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
    # 设置列和行的权重，使得标签可以居中
    success_root.grid_columnconfigure(0, weight=1)
    success_root.grid_columnconfigure(1, weight=1)
    # 设置行的权重，使得行之间均匀分布