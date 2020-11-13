from ftplib import FTP
import os
import sys


def makeAppdir(): # Application을 다운 받을 폴더 생성
    try:
        if not os.path.exists('C:\Remote Install Software/Applications'):
            os.makedirs('C:\Remote Install Software/Applications')
    except OSError:
        pass


def get_list_ftp(ftp, cwd, files = [], directories = []): # ftp 서버의 특정 파일 내부의 파일과 디렉토리를 구함
    data = []
    ftp.cwd(cwd)
    ftp.dir(data.append)
    for item in data:
        pos = item.rfind(' ')
        name = cwd + "/" + item[pos+1:]
        dircheck = item[0:1]
        if dircheck == "d":
            directories.append(name)
            get_list_ftp(ftp,name+"/",files,directories)
        else:
            files.append(name)
    return files, directories


def FTP_download(serverip, down_list): # ftp 서버로부터 특정 디렉토리 안의 파일을 전부 로컬로 다운로드
    with FTP(serverip) as ftp:
        ftp.encoding='utf-8'
        ftp.login()

        download_path = "C:/Remote Install Software/Applications"

        for t in down_list:
            dir_temp = download_path + "/" + t
            if os.path.isdir(dir_temp) is False:
                os.mkdir(dir_temp)

        for i in down_list:
            files, directories = get_list_ftp(ftp,"/"+i)

            for directory in directories:
                dir = download_path + directory

                if os.path.isdir(dir) is False:
                    os.mkdir(dir)

            for file in files:
                with open(download_path + file, 'wb') as localfile:
                    ftp.cwd("/"+i)
                    ftp.retrbinary('RETR ' + "/" + file, localfile.write)