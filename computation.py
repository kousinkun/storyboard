

def decrease(pdata):
    pdata['dec_data'] = pdata['data'].diff()
    print(pdata[['data', 'dec_data']])
