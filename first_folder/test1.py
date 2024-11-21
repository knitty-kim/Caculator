import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets


# form_class = uic.loadUiType("untitled.ui")[0]


class Calculator(QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("untitled.ui", self)

        # self.setupUi(self)

        # 버튼 클릭
        # self.btnConvert.clicked.connect(self.btnFunc)
        # self.btn_2.clicked.connect(self.button2Function)

        self.display = self.findChild(QtWidgets.QLineEdit, "lineEditFrom")
        self.buttons = {
            "0": self.findChild(QtWidgets.QPushButton, "button0"),
            "1": self.findChild(QtWidgets.QPushButton, "button1"),
            "2": self.findChild(QtWidgets.QPushButton, "button2"),
            "3": self.findChild(QtWidgets.QPushButton, "button3"),
            "4": self.findChild(QtWidgets.QPushButton, "button4"),
            "5": self.findChild(QtWidgets.QPushButton, "button5"),
            "6": self.findChild(QtWidgets.QPushButton, "button6"),
            "7": self.findChild(QtWidgets.QPushButton, "button7"),
            "8": self.findChild(QtWidgets.QPushButton, "button8"),
            "9": self.findChild(QtWidgets.QPushButton, "button9"),
            "+": self.findChild(QtWidgets.QPushButton, "buttonAdd"),
            "-": self.findChild(QtWidgets.QPushButton, "buttonSubtract"),
            "*": self.findChild(QtWidgets.QPushButton, "buttonMultiply"),
            "/": self.findChild(QtWidgets.QPushButton, "buttonDivide"),
            "=": self.findChild(QtWidgets.QPushButton, "buttonEqual"),
            "C": self.findChild(QtWidgets.QPushButton, "buttonClear"),
            # "Convert": self.findChild(QtWidgets.QPushButton, "btnConvert"),
        }

        for key, button in self.buttons.items():
            button.clicked.connect(self.create_lambda(key))

    def create_lambda(self, key):
        return lambda _: self.on_button_click(key)

    def on_button_click(self, key):
        if key == "C":
            self.display.clear()  # Clear 버튼
        elif key == "=":
            try:
                expression = self.display.text()
                result = eval(expression)  # 수식 평가
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")  # 에러 처리
        else:
            # 숫자나 연산자를 디스플레이에 추가
            self.display.setText(self.display.text() + key)

    # btn_1이 눌리면 작동할 함수
    # def btnFunc(self):
    #     print("button is clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Calculator()
    myWindow.show()
    app.exec_()
