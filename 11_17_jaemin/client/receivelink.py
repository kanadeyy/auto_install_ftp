import socket
import pickle

def receivelink(serverip): # 서버로 부터 ftp 다운로드할 파일의 목록을 받음
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((serverip,8733))
    data, addr = sock.recvfrom(4096)
    down_list = pickle.loads(data)
    sock.close()

    return down_list