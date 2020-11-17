import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic, Qtcore
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import thumnail
import filelist
import ftp_server
import UDP_Client
import Sendlink
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

        # 배경만들기
        image = QImage("thumbnail.png")
        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.setPalette(palette)

        # 아이콘, 제목 바꾸기
        self.setWindowTitle("Remote install software")
        self.setWindowIcon(QIcon('icon.png'))
        
         #최대화 버튼 없애고 화면크기 고정
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #Close button 이미지 만들기
        self.Closebutton.setStyleSheet('image:url(Close.png);border:0px;')

        # 버튼 이벤트 핸들러 생성
        self.sendbutton.clicked.connect(self.sendbuttonFunction)
        
        self.Closebutton.clicked.connect(self.ClosebuttonFunction)

        #UI에 프로그램과 IP주소 추가
        self.addProgram()
        self.addIP()
        
        # 트레이 아이콘
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setToolTip("RIS Server")
        self.tray_icon.setIcon(QIcon('icon.png'))
        show_action = QAction("열기", self)
        quit_action = QAction("종료", self)
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
    
    def ClosebuttonFunction(self):
        self.hide()
        self.tray_icon.show()
    
    def notify(self, title, message):
        self.tray_icon.showMessage(title, message, 1, 3000)

    def sendbuttonFunction(self):
        selected_IP = self.IpaddressList.selectedItems()
        selected_Item = self.ProgramList.selectedItems()
        if not selected_Item:
            if not selected_IP:
                QMessageBox.warning(self, "Remote Install Software", "내용을 선택하세요")
            else:
                QMessageBox.warning(self, "Remote Install Software", "프로그램을 선택하세요")

        elif not selected_IP:
            QMessageBox.warning(self, "Remote Install Software", "PC를 선택하세요")

        else:
            self.hide()
            self.tray_icon.show()
            SendProgram = []
            for i in selected_Item:
                print(i.text())  # 아이템을 선택하고 send버튼을 눌렀을 때 선택된 아이템들을 출력
                temp = i.text()
                SendProgram.append(temp)

            SendIP = []
            for j in selected_IP:
                print(j.text())
                SendIP.append(j.text())
                
            #보내기버튼 누르면 선택된 아이템 해제
            self.ProgramList.clear()
            self.addProgram()
            self.IpaddressList.clear()
            self.addIP()
            
            self.notify("RIS Server", "파일 업로드 중")
            ftp_server.copyfolder(SendProgram)
            Sendlink.sendlink(SendProgram, SendIP)
            self.notify("RIS Server", "업로드 완료")
                              
            return SendProgram, SendIP

    def addProgram(self):
        z, x, y = filelist.duplecheck()
        for i in x:
            self.ProgramList.addItem(i)

    def addIP(self):
        global IPaddress_global
        for i in IPaddress_global:
            self.IpaddressList.addItem(i)    
    
if __name__ == "__main__":
    ftp_server.makeFTPdir()
    global IPaddress_global
    IPaddress_global = UDP_Client.received_data()

    srv = threading.Thread(target=ftp_server.FTPserver)
    srv.daemon = True
    srv.start()
    
    thumnail.Open_IntroImage()    
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    filelist.duplecheck()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
