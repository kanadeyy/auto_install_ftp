import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import time


form_class1 = uic.loadUiType("image_UI.ui")[0]

class UIwindow(QDialog, form_class1):
    def __init__(self):
        super().__init__()
        self.initUI()

        self.setWindowTitle("Remote install software")
        self.setWindowIcon(QIcon('icon.png'))

    def initUI(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.lbl = QLabel(self)
        self.lbl.resize(675, 400)
        pixmap = QPixmap("thumbnail.png")
        self.lbl.setPixmap(QPixmap(pixmap))
        self.resize(675, 400)
        self.show()

def Open_IntroImage():
    app = QApplication(sys.argv)
    # WindowClass의 인스턴스 생성
    myWindow = UIwindow()
    time.sleep(3)
    QCoreApplication.quit()