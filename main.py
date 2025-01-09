import gui

try:
    import pyi_splash
    import time

    for i in range(100):
        text = f"加载中……进度{i}%"
        time.sleep(0.1)  # 模拟一个速度比较慢的加载过程

        pyi_splash.update_text(text)  # 更新显示的文本

    pyi_splash.close()  # 关闭闪屏

except ImportError:
    pass

#画面を起動する

sbtool_start = gui.GUI(callback=gui.process_data)

#ボタン画面を表示
sbtool_start.interface()

# 启动 GUI 主事件循环
sbtool_start.mainroot.mainloop()




