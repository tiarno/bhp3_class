## Welcome to class 2!

### Black Hat Python3 

### Raleigh ISSA

---

# Summary from last class

- mapping an app
- word lists for enumeration
- word lists for password bruteforce
- browser tools
- `lxml` for web parsing

---

## A note on iterating a queue

You can't do it that way :-)

---

## A note on `lxml`

General notes and demo

---

```python
from lxml import etree
url = 'http://www.textfiles.com/hacking/INTERNET'
parser = etree.HTMLParser()
tree = etree.parse(url, parser=parser)
headelem = tree.find('//h1')
print(headelem.text)

for elem in tree.findall('//a'):
    if elem.get('href'):
        print(f'{elem.text:<20} {url}/{elem.get("href")}')

---

## Exception Handling

https://www.pythonforthelab.com/blog/learning-not-to-handle-exceptions/

---

## Sockets

https://github.com/crazyguitar/pysheeet/blob/master/docs/notes/python-socket.rst

---

## IP Headers

- diagram
- icmp diagram
- ipheader_struct.py
- ipheader_c.py

---

# icmp headers

- ping
- traceroute

---

# ipaddress package

---

# UDP Scanner

- how it works

---

write the scanner

---

test the scanner

---

# Reading#

https://codingsec.net/2016/05/decoding-ip-layer-python/

http://www.ciscopress.com/articles/article.asp?p=348253&seqNum=4

https://wiki.wireshark.org/InternetProtocolFamily

https://code.activestate.com/recipes/576662-icmplib/

https://code.activestate.com/recipes/409689-icmplib-library-for-creating-and-reading-icmp-pack/

https://docs.python.org/3/library/struct.html#format-characters

https://docs.python.org/3.5/library/ctypes.html#ctypes.Structure


http://www.firewall.cx/networking-topics/protocols/icmp-protocol/153-icmp-destination-unreachable.html

https://michieldemey.be/blog/network-discovery-using-udp-broadcast/


---

## Other stuff

res, unans = traceroute(['reachtim.com'], dport=[443], maxttl=20, retry=-2)

res.graph()

hosts = ['www.microsoft.com', 'www.cisco.com', 'www.yahoo.com', 'www.wanadoo.fr', 'www.pacsec.com']

res, unans = traceroute(hosts, dport=[80,443], maxttl=20, retry=-2)


a = Ether()/IP(dst="www.slashdot.org")/TCP()/"GET /index.html HTTP/1.0 \n\n"

hexdump(a)

a[0].pdfdump(layer_shift=1)