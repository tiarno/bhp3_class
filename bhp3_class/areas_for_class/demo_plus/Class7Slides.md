## Welcome to class 7!

### Black Hat Python3 

### Raleigh ISSA

---

## Github repo

https://github.com/tiarno/bhp3_class

---

## Summary from last class

- scapy graphics + world map
- arp poisoning + dns spoofing
- building images from packet capture streams
- identify faces in those captured images

---

## Extract content from pcap file

`recapper.py`

---

## Python coding

- named tuple
- dictionary creation
- regular expression/raw strings
- string slicing/indexing
- interating dict keys
- byte/string conversion

---

## RegExp

- https://pythex.org


---

## HTTP headers
- https://developer.mozilla.org/en-US/docs/Glossary/MIME_type

---

## Clients and Servers

- TCP Client: foundation for sending and receiving
- TCP Server: foundation for creating, listening, sending, receiving
- UDP Client / UDP Server
- TCP Proxy: machine-in-the-middle, leveraging the TCP client/server code

---

## TCP Client

- first, a quick http server: python -m http.server --bind=9999

---

## TCP Client

```python
import socket

def connect(host, port):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send('GET /')
    return client.recv(4096)

if __name__ == '__main__':
    host = '192.168.1.69'
    port = 9999
    print(connect(host, port))
```

---

- server `tcp_server.py`
- client `tcp_client.py`


--- 

# NetCat

- `netcat.py`

---

## Hexdump

```
          1         2
012345678901234567890123456789
 Black Hat Python, Raleigh ISSA
:Black Hat :
s = 'Black Hat '
hexa = ' '.join(['%04X' % ord(x) for x in s])
0042 006C 0061 0063 006B 0020 0048 0061 0074 0020
text = ''.join([x if 32 <= ord(x) < 127 else '.' for x in s])
'Black Hat '
```


---

## Your Job

- Finish out your `recapper.py`
- Test it with the newly added `pcap.pcap` file
- Start building out your version of `netcat.py`

---

## Reading

- NetCat `ncat`, `nc`: the real thing and how it works
  https://www.binarytides.com/netcat-tutorial-for-beginners/
  http://forensicswiki.org/wiki/Netcat
  http://forensicswiki.org/wiki/Tcpdump#Using_Tcpdump_with_Netcat

---

## Feedback please!

- tim@reachtim.com
- discord: https://discord.gg/WR23qUj

 