import sys
from Day01.designer.MainWindow_ui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

if __name__ == '__main__':
    # 创建 Qapplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.setWindowTitle("第二个窗体")
    mainWindow.show()
    # 进入程序的主循环 并通过 exit函数保证主循环安全结束
    sys.exit(app.exec_())
