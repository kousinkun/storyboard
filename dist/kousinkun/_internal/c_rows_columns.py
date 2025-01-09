
import pandas as pd
import numpy as np
import os


def changecolumn(pdata, number, text):
    if not isinstance(number, int):
        raise ValueError('The first parameter must be a number.')
    if not isinstance(text, str):
        raise ValueError("The second parameter must be a string.")
    pdata.insert(loc=number, column=text, value='0')
