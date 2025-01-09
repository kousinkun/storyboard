import pandas as pd
import numpy as np
import os

#列名を作る插入一个行
def header(pdata):
    #列的长度
    num_columns = len(pdata.columns)
    if(num_columns < 7):
        #制作一个列头名字
        new_header = ['Column1', 'Column2', 'data', 'Column4', 'Column5', 'Column6']
        #判断制作的列头名字和实际列匹配
        if len(new_header) != num_columns:
            print("列数不匹配！将根据实际列数修改列名")
            # 只保留与列数匹配的部分
            new_header = new_header[:num_columns]
            #制作
            pdata.columns = new_header



# 初期化
def initialization(pdata):
    #列を特定
    stordyboard_time = pdata.iloc[:, 2]
    # 初期化値はnullの場合は0になる
    stordyboard_time.fillna(0, inplace=True)
    # 初期化、符号を削除
    if 'data' in pdata.columns:
        pdata['data'] = pdata['data'].str.replace(r'[\[\]]', '', regex=True)
    else:
        print("Column 'data' not found!")
    # 检查数据是否为数值类型
    pdata['data'] = pd.to_numeric(pdata['data'], errors='coerce')

