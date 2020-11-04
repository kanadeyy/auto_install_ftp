import socket


def getipmac():
    macaddr = socket.gethostbyaddr(socket.gethostname())
    ipaddr = socket.gethostbyname(socket.gethostname())

    return ipaddr, macaddr
