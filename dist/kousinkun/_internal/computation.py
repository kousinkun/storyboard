import pandas as pd
import numpy as np
import os

def decrease(pdata):
    pdata['dec_data'] = pdata['data'].diff()
    print(pdata[['data', 'dec_data']])
