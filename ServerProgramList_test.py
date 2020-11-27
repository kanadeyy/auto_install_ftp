import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
import getipmac
import PC_ID
import UDP_Server
import receivelink
import ftp_client
import threading
import time

form_class = uic.loadUiType("ServerProgramList.ui")[0]

class WindowClass1(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 배경만들기
        image = QImage("thumbnail.png")
        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.setPalette(palette)

        # 제목표시줄 없애기
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # Close Button 이미지 만들기
        self.CloseButton.setStyleSheet('image:url(Close.png);border:0px;')

        #트리거 생성
        # self.ReceiveButton.clicked.connect(self.ReceiveButtonFunction)
        self.CloseButton.clicked.connect(self.CloseButtonFunction)

        #UI에 프로그램 리스트 추가
        self.addProgram()

    def CloseButtonFunction(self):
        self.hide()

    def ReceiveButtonFunction(self):
        selected_Item = self.ProgramList.selectedItems()
        if not selected_Item:
            QMessageBox.warning(self, "Remote Install Software", "내용을 선택하세요")

        else :
            self.hide()
            self.tray_icon.show()
            SendProgram = []
            for i in selected_Item:
                print(i.text())  # 아이템을 선택하고 send버튼을 눌렀을 때 선택된 아이템들을 출력
                temp = i.text()
                SendProgram.append(temp)

        self.ProgramList.clear()
        self.addProgram()

    def addProgram(self):
        # z, x, y = filelist.duplecheck()
        x = ['ex1','ex2','ex3','ex4']
        for i in x:
            self.ProgramList.addItem(i)

if __name__ == "__main__":
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass1()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()