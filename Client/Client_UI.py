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

form_class = uic.loadUiType("Client_UI.ui")[0]
global Serverip
Serverip = "null"

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 배경만들기
        image = QImage("thumbnail.png")
        palette = QPalette()
        palette.setBrush(10, QBrush(image))
        self.setPalette(palette)

        #아이콘, 제목
        self.setWindowTitle("Remote install software")
        self.setWindowIcon(QIcon('icon.png'))

        ID = PC_ID.file_read()
        IP,MAC = getipmac.getipmac()
        self.iptext.append(IP)
        self.idtext.append(ID)

        ID_ = self.IP_Change_Edit.text()

        # 트리거 만들기
        self.okbutton.clicked.connect(self.okbuttonFunction)
        self.IP_Change_Edit.returnPressed.connect(self.okbuttonFunction)

        # 제목표시줄 없애기
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        #트레이아이콘
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('icon.png'))
        self.tray_icon.setToolTip("RIS Client")
        show_action = QAction("정보 보기", self)
        quit_action = QAction("종료", self)
        show_action.triggered.connect(self.show)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        trayDouble = self.tray_icon.activated
        trayDouble.connect(self.trayDoubleclick)
        self.tray_icon.show()

    def trayDoubleclick(self, reason):
        if reason == 2:
            self.show()

    def notify(self, title, message):
        self.tray_icon.showMessage(title, message, 1, 3000)

    def okbuttonFunction(self):
        ID_ = self.IP_Change_Edit.text()
        if not ID_:
            QMessageBox.warning(self,"Remote Install Software","메세지를 입력하세요") #https://pythonprogramminglanguage.com/pyqt5-message-box/

        else :
            PC_ID.file_modify(ID_)
            self.idtext.clear()
            self.IP_Change_Edit.clear()
            self.idtext.append(ID_)

    def closeEvent(self, event):
        event.ignore()
        self.hide()


def udpcommunicationforever():
    global Serverip
    while True:
        Serverip = UDP_Server.send_data()

def udp_recv_ftp_download():
    global recv_link
    recv_link = []
    while True:
        if Serverip != "null":
            recv_link.append(receivelink.receivelink(pcip))
        else:
            pass

def ftp_downforever():
    global recv_link
    while True:
        try:
            ftp_link = recv_link.pop(0)
            traynotification = WindowClass()
            traynotification.notify("RIS Client", "설치 시작")
            ftp_client.FTP_download(Serverip, ftp_link)
            traynotification.notify("RIS Client", "설치 완료")
            time.sleep(5)
        except:
            pass

if __name__ == "__main__":
    global pcip
    pcip, pcmac = getipmac.getipmac()
    ftp_client.makeAppdir()

    srv = threading.Thread(target=udpcommunicationforever)
    srv.daemon = True

    srv2 = threading.Thread(target=udp_recv_ftp_download)
    srv2.daemon = True

    srv3 = threading.Thread(target=ftp_downforever)
    srv3.daemon = True

    srv.start()
    srv2.start()
    srv3.start()

    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    #myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
