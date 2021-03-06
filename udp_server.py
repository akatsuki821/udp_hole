import socket
import sys
from util import *

addresses = []


def main(host="", port=7000):
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((host, port))
    print("Listening on: " + str(port))
    while True:
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("connection from: %s", addr)
        addresses.append(addr)
        if len(addresses) >= 2:
            print("server - send client info to: %s", addresses[0])
            sock.sendto(addr_to_msg(addresses[1]), addresses[0])
            print("server - send client info to: %s", addresses[0])
            sock.sendto(addr_to_msg(addresses[0]), addresses[1])
            addresses.pop(1)
            addresses.pop(0)


if __name__ == '__main__':
    main(*addr_from_args(sys.argv))
