import pandas as pd
import c_rows_columns
from io import StringIO
import meassage
# 初期化数据过滤
def initialization(file_path):

    # 读取文件并去掉每行末尾的逗号
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines = [line.replace(',', '') for line in lines]  #     使用 replace 去除每行末尾的逗号
    cleaned_content = ''.join(lines)      # 将处理后的行合并为一个字符串

    # 使用 StringIO 将字符串转换为类文件对象
    cleaned_content_io = StringIO(cleaned_content)
    # 使用 StringIO 将字符串转换为类文件对象
    pdata = pd.read_csv(cleaned_content_io, names=['og_data'], on_bad_lines='warn')

    #读取错误行
    missing_data = pdata[pdata.isna().any(axis=1)]
    if not missing_data.empty:
        print(missing_data)
        pdata = meassage.Error.process_data_null
    else:
        "利用分割函数来对数据进行分组"
        pdata = c_rows_columns.base_grouping(pdata)
        "检查value列"
        value_check(pdata)
        "检查message列"
        message_check(pdata)
    return pdata

# 清空背景颜色
def clear_button_background(*buttons):
    # 遍历所有传入的按钮，恢复它们的背景颜色
    for button in buttons:
        button.config(bg="SystemButtonFace")


def value_check(pdata):
    # 列を特定列初期化、符号を削除
    stordyboard_time = pdata.iloc[:, 3]
    # 初期化値はnullの場合は0になる
    stordyboard_time.fillna(0, inplace=True)
    if 'value' in pdata.columns:
        pdata['value'] = pdata['value'].str.replace(r'[\[\]]', '', regex=True)
    else:
        print("Column 'value' not found!")
    # 检查数据是否为数值类型
    pdata['value'] = pd.to_numeric(pdata['value'], errors='coerce')


def message_check(pdata):
    #检查是否有无效公式
    if 'message' in pdata.columns:
        # 遍历 'message' 列中的每一行
        for index, message in pdata['message'].items():  # 直接遍历 'message' 列
            if isinstance(message, str) and '===' in message:  # 检查是否包含 '=='
                print(f"行 {index + 1} 的 message 列包含 '==='： {message}")
                # 在此处可以对该行的数据进行处理，比如修改或清除
                pdata.at[index, 'message'] = ' ' + message
                # pdata.at[index, 'message'] = None  # 如果需要清除该行的值，可以使用这个方法
            elif isinstance(message, str) and 'invalid' in message:
                pdata = meassage.Error.process_data_formula

    return pdata
    # 输出处理后的 DataFrame（如果进行了修改）




