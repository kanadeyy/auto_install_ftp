#파일을 보냄
import socket
import threading
import time

def received_data():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
    client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Enable broadcasting mode
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    IP_address = []
    PC_ID = []
    order = 'key'

    client.bind(('', 8371))
    print("send broadcast!")

    while True:
        #특정 메시지(key)를 보냄
        # client.sendto(order.encode(),('<broadcast>',8731))
        # print("특정 메세지 보냄")

        #서버로부터 IP,ID를 받음
        data, addr = client.recvfrom(1024)
        # print("received IP_address,PC_ID: %s"%data.decode())  # data.decode()
        IPadd, PCID = data.decode().split(',')
        print('IPaddress =', IPadd)
        print('PC_ID =', PCID)
        time.sleep(3)
        IP_address.append(IPadd)
        PC_ID.append(PCID)
        client.sendto(data,addr)

    return IP_address, PC_ID

received_data()
