import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5 import uic
import getipmac
from client import PC_ID
from client import UDP_Server
from client import receivelink
from client import ftp_client
import threading


form_class = uic.loadUiType("Client_UI.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        ID = PC_ID.file_read()
        IP,MAC = getipmac.getipmac()
        self.iptext.append(IP)
        self.idtext.append(ID)

        ID_ = self.IP_Change_Edit.text()

        self.okbutton.clicked.connect(self.okbuttonFunction)
        self.IP_Change_Edit.returnPressed.connect(self.okbuttonFunction)


        #트레이아이콘
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon('icon.png'))
        show_action = QAction("정보 보기", self)
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

    def okbuttonFunction(self):
        ID_ = self.IP_Change_Edit.text()
        if not ID_:
            QMessageBox.about(self,"경고","메세지를 입력하세요") #https://pythonprogramminglanguage.com/pyqt5-message-box/

        else :
            PC_ID.file_modify(ID_)
            self.idtext.clear()
            self.IP_Change_Edit.clear()
            self.idtext.append(ID_)

    def closeEvent(self, event):
        event.ignore()
        self.hide()


def protocol():
    ftp_client.makeAppdir()
    ID = PC_ID.file_read()
    Serverip = UDP_Server.send_data(ID)
    traynotification = WindowClass()
    while True:
        recv_link = receivelink.receivelink(Serverip)
        traynotification.notify("RIS Client","설치 시작")
        ftp_client.FTP_download(Serverip,recv_link)
        traynotification.notify("RIS Client", "설치 완료")

if __name__ == "__main__":

    srv = threading.Thread(target=protocol)
    srv.daemon = True
    srv.start()

    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    # 프로그램 화면을 보여주는 코드
    #myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()