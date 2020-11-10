import socket
import pickle

def receivelink(serverip):
    serverip = '192.168.0.6'
    list = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((serverip,8733))
    data, addr = sock.recvfrom(4096)
    list = pickle.loads(data)
    print(list)

    return list
