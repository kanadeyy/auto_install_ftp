import socket


def getipmac(): # 현재 PC의 IP address와 MAC address를 구함
    macaddr = socket.gethostbyaddr(socket.gethostname())
    ipaddr = socket.gethostbyname(socket.gethostname())

    return ipaddr, macaddr
