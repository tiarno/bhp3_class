#!/usr/bin/env python
import socket
import sys

def serve(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('127.0.0.1', port))
    print(f'waiting on port: {port}')
    while True:
        try:
            data, addr = s.recvfrom(1024)
            print(addr)
            print(data.decode())
            s.sendto(b'okay', addr)
        except KeyboardInterrupt:
            print('Interupted by user. Exiting.')
            sys.exit()

if __name__ == '__main__':
    port = 9999
    serve(port)
