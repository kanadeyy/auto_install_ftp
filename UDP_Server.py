#파일을 받음
import socket
import getipmac
import time

def send_data(ID):
    IP_address, mymac = getipmac.getipmac()
    PC_ID = ID
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(('',8731))
    data,addr = sock.recvfrom(1024)
    check,Serverip = data.decode('utf-8').split(",")

    sock.close()

    if check == "RIS":
        time.sleep(2)
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        message = IP_address + "," + PC_ID
        sock2.sendto(message.encode('utf-8'),(Serverip,8732))
        print('데이터 보냄')
        sock2.close()

send_data('PC1')
