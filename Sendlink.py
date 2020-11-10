import socket
import pickle

def sendlink(SendProgram,selectedip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = pickle.dumps(SendProgram)
    for i in selectedip:
        sock.sendto(data, (i, 8733))