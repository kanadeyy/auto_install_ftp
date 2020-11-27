import socket
import pickle
import filelist

def sendServerprogramlist(IPaddress_global):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    final_buffer, programlist, programlocation = filelist.duplecheck()
    data = pickle.dumps(programlist)
    userip = IPaddress_global
    str_userip = ','.join(userip)
    ip = str_userip.split(',')
    sendip = ip[0]
    sock.sendto(data, (sendip, 8740))
    sock.close()


def receiveduserselectedprogram(IPaddress_global):
    userip = IPaddress_global
    str_userip = ','.join(userip)
    ip = str_userip.split(',')
    sendip = ip[0]
    print(sendip)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((sendip,8741))
    data, addr = sock.recvfrom(4096)
    userselectedprogram = pickle.loads(data)
    sock.close()

    return userselectedprogram, sendip