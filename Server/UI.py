import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import filelist
import ftp_server
import errno, os, winreg
from os import unlink
# from PIL import Image
import time
# import ftp_client
import UDP_Client
import Sendlink
import getipmac
import threading


# UI파일 연결
# 단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("grad_UI.ui")[0]
global IPaddress_global


# 화면을 띄우는데 사용되는 Class 선언


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.sendbutton.clicked.connect(self.sendbuttonFunction)
        z, x, y = filelist.duplecheck()
        for i in x:
            self.ProgramList.addItem(i)  # ProgramList.py 에서의 list를 받아 Widget에 추가

        global IPaddress_global
        for i in IPaddress_global:
            IPaddress_global = self.IpaddressList.addItem(i)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('icon.png'))
        show_action = QAction("열기", self)
        quit_action = QAction("종료", self)
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def notify(self, title, message):
        self.tray_icon.showMessage(title, message, 1, 3000)

    def sendbuttonFunction(self):
        self.hide()
        selected_Item = self.ProgramList.selectedItems()
        SendProgram = []
        for i in selected_Item:
            print(i.text())  # 아이템을 선택하고 send버튼을 눌렀을 때 선택된 아이템들을 출력
            temp = i.text()
            SendProgram.append(temp)

        selected_IP = self.IpaddressList.selectedItems()
        SendIP = []
        for j in selected_IP:
            print(j.text())
            SendIP.append(j.text())
        self.notify("RIS Server", "파일 업로드 중")
        ftp_server.copyfolder(SendProgram)
        Sendlink.sendlink(SendProgram, SendIP)
        self.notify("RIS Server", "업로드 완료")

        return SendProgram, SendIP

    def closeEvent(self, event):
        event.ignore()
        self.hide()


if __name__ == "__main__":

    ftp_server.makeFTPdir()
    global IPaddress_global
    IPaddress_global = UDP_Client.received_data()

    srv = threading.Thread(target=ftp_server.FTPserver)
    srv.daemon = True
    srv.start()
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    filelist.duplecheck()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()