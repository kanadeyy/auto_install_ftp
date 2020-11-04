import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import filelist
import ftp_server
import errno, os, winreg
from os import unlink
from PIL import Image
import time

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("grad_UI.ui")[0]

#화면을 띄우는데 사용되는 Class 선언


class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.sendbutton.clicked.connect(self.sendbuttonFunction)
        z, x, y = filelist.duplecheck()
        for i in x:
            self.ProgramList.addItem(i)  # ProgramList.py 에서의 list를 받아 Widget에 추가

    def sendbuttonFunction(self):
        selected_Item = self.ProgramList.selectedItems()
        SendProgram = []
        for i in selected_Item:
            print(i.text()) #아이템을 선택하고 send버튼을 눌렀을 때 선택된 아이템들을 출력
            temp = i.text()
            SendProgram.append(temp)

        #print(list_test)
        try:
            if not os.path.exists('C:\Remote Install Software/temp'):
                os.makedirs('C:\Remote Install Software/temp')
        except OSError:
            pass

        #filePath = 'C:/Remote Install Software/temp/sel_program.txt'
        #f = open(filePath,"w")
        #f.write(str(SendProgram))
        #f.close()

        print(ftp_server.copyfolder(SendProgram))

        return SendProgram


if __name__ == "__main__" :

    # image= Image.open('표지.png')
    # image.thumbnail((600,600))
    # image.save('표지.png')
    # image_ = Image.open('표지.png')
    # image_.show()
    # time.sleep(3)
    # image_.close()

    ftp_server.makeFTPdir()
    filelist.duplecheck()
    # ftp_server.FTPserver()

    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

