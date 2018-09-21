#!/usr/bin/env python
import socket
import sys
import threading

def create(ip='127.0.0.1', port=5555):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print(f'[*] Listening on {ip}:{port}')
    return server

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f'[*] Received: {request}')
    if (request == b'Tell me a secret'):
        client_socket.send(b"I like biscuits.")
    client_socket.send(b"ACK!")
    

def serve(server):
    while True:
        try:
            print('looping...')
            client_socket, addr = server.accept()
            print(addr)
            print(f'[*] Accepted connection from: {addr[0]}{addr[1]}')

            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
        except KeyboardInterrupt:
            print('Interupted by user. Exiting.')
            client_socket.close()
            sys.exit()

if __name__ == '__main__':
  server = create()
  serve(server)
