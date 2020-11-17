import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import getipmac
from distutils.dir_util import copy_tree
import filelist
import time

serverip, servermac = getipmac.getipmac()
FTP_HOST = serverip
FTP_PORT = 21
FTP_DIRECTORY = os.path.join(os.getcwd(), "C:\Remote Install Software/FTPserver")


def makeFTPdir(): # FTP 서버 폴더 생성
    try:
        if not os.path.exists('C:\Remote Install Software/FTPserver'):
            os.makedirs('C:\Remote Install Software/FTPserver')
    except OSError:
        pass


def FTPserver(): # FTP 서버 실행
    authorizer = DummyAuthorizer()

    authorizer.add_anonymous(FTP_DIRECTORY)

    handler = FTPHandler
    handler.banner = "RIS FTP Server."

    handler.authorizer = authorizer
    handler.passive_ports = range(60000, 65535)

    address = (FTP_HOST, FTP_PORT)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 30

    server.serve_forever()


def copyfolder(SendProgram): # FTP 서버로 지정할 파일에 UI에서 선택한 파일을 복사
    final_buffer, programlist, programlocation = filelist.duplecheck()
    ftplocation = "C:/Remote Install Software/FTPserver/"
    selectedprogram = SendProgram
    selectedlocation = []
    temp_index = []
    success_sign = 10

    for i in range (0,len(selectedprogram)):
        temp_index.append(int(programlist.index(selectedprogram[i])))

    for i in range (0,len(temp_index)):
        t = temp_index[i]
        selectedlocation.append(programlocation[t])

    for i in range (0,len(selectedprogram)):
        destlocation = ftplocation + str(selectedprogram[i])
        copy_tree(selectedlocation[i], destlocation)

        while True:
            time.sleep(5)
            if get_dir_size(path=selectedlocation[i]) == get_dir_size(path=destlocation):
                break
            else:
                continue

    return selectedlocation


def get_dir_size(path='.'): # 폴더 사이즈 구하기
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total