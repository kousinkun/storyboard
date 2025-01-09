import pandas as pd
import re

# 定义分割函数
def split_data(line):

    # 匹配每一行的结构
    match = re.match(r"(\[\d+\s[\d:.]+\])\s*(\S+\[[^\]]+\])\s*(\[\s*\d+\.\d+\])\s*(.*)", line)

    if match:
        # 提取四个部分
        timestamp = match.group(1)
        label = match.group(2)
        value = match.group(3)
        message = match.group(4)  # 剩余的部分作为消息内容

        return timestamp, label, value, message
    else:
        return pd.Series([None, None, None, None])

# 利用分割函数来对数据进行分组分成四列

def base_grouping(pdata):
    pdata = pdata[['timestamp', 'label', 'value', 'message']] = pdata['og_data'].apply(lambda x: pd.Series(split_data(x)))
    return pdata