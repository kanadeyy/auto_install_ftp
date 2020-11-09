import socket
import getipmac
import time

myip, mymac = getipmac.getipmac()
ID = "내 PC"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('',9980))
data,addr = sock.recvfrom(1024)
print(data.decode('utf-8'))
check,Serverip = data.decode('utf-8').split(",")
print(check)
print(Serverip)
sock.close()

if check == "I am Server":
    time.sleep(3)
    sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = myip + "," + ID
    sock2.sendto(message.encode('utf-8'),(Serverip,9981))
    sock2.close()