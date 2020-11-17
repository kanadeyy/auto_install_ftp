import socket
import getipmac
import time

def send_data(ID): # 서버로 부터 RIS 메시지 수신시 자신의 IP와 PC의 ID 송신
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

    return Serverip