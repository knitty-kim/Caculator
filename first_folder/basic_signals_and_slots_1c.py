import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)


class MainWindow(QMainWindow):  # 부모 클래스를 인자에 넣기
    def __init__(self):
        super().__init__()  # 상속을 받는다는 의미

        # self란? ; 클래스 자신의 "인스턴스 매개변수"
        self.setWindowTitle("MY APP")
        # super().setWindow..하지 않는 이유는
        # 1. 현재 MainWindow 클래스를 정의하고 있는 상황이기 떄문에
        # 2. self로 자신의 인스턴스 변수에 접근하여 상속받은 메서드를 사용하는게 옳지
        #    이유없이 super().setWindow..로 부모 클래스에 접근하는건 옳지 않다
        # super()란 ; 부모 클래스의 메서드나 속성을 호출할 때 사용하는 내장 함수

        # 원하는 변수 생성 및 초기화
        self.button_is_checked = True

        button = QPushButton("PRESS ME!")

        # 버튼 세팅
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_toggled)
        button.setChecked(self.button_is_checked)

        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
