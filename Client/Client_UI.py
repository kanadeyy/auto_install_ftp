import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import getipmac


form_class = uic.loadUiType("Client_UI.ui")[0]


# fr = open('PC_ID.txt','r')
# fw = open('PC_ID.txt','w')
# text = fr.read()
#
# if text == 'temp':
#     ID = 'unknown'
# elif text != 0:
#     ID = text
#
# print('ID = '+ID)

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ID = 'unknown'
        IP,MAC = getipmac.getipmac()
        self.iptext.append(IP)
        self.idtext.append(ID)

        self.okbutton.clicked.connect(self.okbuttonFunction)
        self.IP_Change_Edit.returnPressed.connect(self.okbuttonFunction)

    def okbuttonFunction(self):
        ID_ = self.IP_Change_Edit.text()
        self.idtext.clear()
        self.IP_Change_Edit.clear()
        self.idtext.append(ID_)
        # fw.write(ID_)


if __name__ == "__main__":

    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
