import socket
import getipmac
import time
import PC_ID

def send_data(): # 서버로 부터 RIS 메시지 수신시 자신의 IP와 PC의 ID 송신
    IP_address, mymac = getipmac.getipmac()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind(('',8731))
    data,addr = sock.recvfrom(1024)
    check,Server_ip = data.decode('utf-8').split(",")

    sock.close()

    if check == "RIS":
        time.sleep(2)
        sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        PCID = PC_ID.file_read()
        message = IP_address + "," + PCID
        sock2.sendto(message.encode('utf-8'),(Server_ip,8732))
        sock2.close()

    return Server_ip