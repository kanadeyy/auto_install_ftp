#파일을 받음
import socket
import time
import threading
import getipmac

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

server.bind(('', 8371))
# server.settimeout(0.2)

IP_address, mac_address = getipmac.getipmac()
PC_ID = 'PC1' # PC IP를 입력받는 부분/ 임시데이터
message = IP_address+','+PC_ID
print(message)

# order, add = server.recvfrom(2048)
# if( ):


while True:
    # 클라이언트에서 특정 메세지를 받음
    # data, addr = server.recvfrom(2048)
    # print('key: ', data.decode())

    # 만약 그 데이터가 맞다면
    # if data != 0:
    server.sendto(message.encode('utf-8'), ('<broadcast>', 8371))
    print("send message")
    data,addr = server.recvfrom(1024)
    time.sleep(3)
    # if data == message.decode():
    #     break
    # else :
    #     print('특정 메세지 수신을 기다리는중')
    #     time.sleep(1)
