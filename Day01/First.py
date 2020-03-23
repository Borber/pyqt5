import sys
from PyQt5.QtWidgets import QApplication,QWidget


if __name__ == '__main__':
    # 创建 Qapplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置尺寸
    w.resize(300, 150)
    # 窗口位置
    w.setWindowTitle("第一个Pyqt窗口")
    # 显示窗口
    w.show()
    # 进入程序的主循环 并通过 exit函数保证主循环安全结束
    sys.exit(app.exec_())
