#!/usr/bin/env python
import socket

def client(host='127.0.0.1', port=9999):
  client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  print('sending....')
  client.sendto(b"Tell me a ecret",(host, port))
  print('sent')
  
  data, addr = client.recvfrom(4096)
  print('received')
  return (data, addr)


if __name__ == '__main__':
  data, addr = client()
  print(f'data is {data}')
  print(f'addr is {addr}')
