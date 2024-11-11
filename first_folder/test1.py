import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("untitled.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 버튼 클릭
        self.btnConvert.clicked.connect(self.btnFunc)
        # self.btn_2.clicked.connect(self.button2Function)

    # btn_1이 눌리면 작동할 함수
    def btnFunc(self):
        print("button is clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
