

def output_csv():
    print('not build')

def output_excel(output_path, pdata):
    try:
        pdata.to_excel(output_path, index=False)  # 保存到新文件，不保存行索引
        print(f"\n数据已保存到: {output_path}")

        return
    except Exception as e:
        return f"Error: Unable to read the file. Details: {e}"

def output_txt():
    print('not build')