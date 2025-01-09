
import pandas as pd
import numpy as np
import os

def read_csv(fpath):
    pdata = pd.read_csv(fpath, delimiter="]", on_bad_lines="skip", header=None)
    print(f"\n数据を開け: {fpath}")

    return pdata
def read_excel(fpath):
    try:
        pdata = pd.read_excel(fpath, header=None)
        print(f"\n数据を開け: {fpath}")

        return pdata
    except Exception as e:
        return f"Error: Unable to read the file. Details: {e}"

def read_txt():
    print('not build')