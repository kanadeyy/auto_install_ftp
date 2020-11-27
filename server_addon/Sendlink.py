import socket
import pickle

def sendlink(SendProgram,selectedip): # client로 udp를 이용하여 받아야 하는 파일 정보 전송
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = pickle.dumps(SendProgram)
    sendip = []
    for t in selectedip:
        split_ip = t.split(',')[0]
        sendip.append(split_ip)

    for i in sendip:
        sock.sendto(data, (i, 8733))
    sock.close()

def sendlinktoaddon(SendProgram,selectedip): # client로 udp를 이용하여 받아야 하는 파일 정보 전송
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = pickle.dumps(SendProgram)
    sock.sendto(data, (selectedip, 8733))
    sock.close()