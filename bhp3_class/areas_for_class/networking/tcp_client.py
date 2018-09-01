#!/usr/bin/env python
import socket

def client(host='www.google.com', port=80):
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect((host, port))

  # Note the b for bytestring.
  # client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
  client.send(b"Tell me a secret")
  
  return client.recv(4096)

if __name__ == '__main__':
  data = client('127.0.0.1', 5555)
  print(data)
