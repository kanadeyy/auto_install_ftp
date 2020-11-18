import socket
import getipmac

def received_data(): # RIS 메시지 broadcasting 한 뒤 ack를 list로 저장
    IP_address, mymac = getipmac.getipmac()
    list = []
    checkmsg = "RIS"+ "," + IP_address

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)
    sock.sendto(checkmsg.encode('utf-8'),('255.255.255.255',8731))

    sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock2.bind((IP_address, 8732))
    sock2.settimeout(3)

    while True:
        try:
            data, addr = sock2.recvfrom(1024)
            list.append(data.decode('utf-8'))
        except:
            break
            
    sock.close()
    sock2.close()

    return list
