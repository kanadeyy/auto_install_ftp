import socket
import pickle

def sendlink(SendProgram,selectedip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = pickle.dumps(SendProgram)
    sendip = []
    for t in selectedip:
        split_ip = t.split(',')[0]
        sendip.append(split_ip)

    for i in sendip:
        sock.sendto(data, (i, 8733))

    sock.close()