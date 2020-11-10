import socket
import pickle

def receivelink(serverip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((serverip,8733))
    data, addr = sock.recvfrom(4096)
    down_list = pickle.loads(data)
    sock.close()
    return down_list

