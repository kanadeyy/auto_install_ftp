import socket
import getipmac
import time

myip, mymac = getipmac.getipmac()
ID = "내 PC"
message = myip+ID
list = []
checkmsg = "I am Server"+ "," + myip
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)
sock.sendto(checkmsg.encode('utf-8'),('192.168.0.255',9980))
#sock.close()

sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2.bind((myip, 9981))

#start = time.time()
while True:
    #sock2.settimeout(1)
    data, addr = sock2.recvfrom(1024)
    list.append(data.decode('utf-8'))
    print(list)


sock.close()
sock2.close()
