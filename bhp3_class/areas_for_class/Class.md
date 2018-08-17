## Welcome to class 6!

### Black Hat Python3 

### Raleigh ISSA

---

## Github repo

https://github.com/tiarno/bhp3_class

---

## Summary from last class
 
- scapy w/graphics
- bpf
- arp watch/poison
- three-way handshake
- named tuples

---

## Three-way Handshake

- on client:
    - `iptables -t filter -I OUTPUT -p tcp --sport 10000 --tcp-flags RST RST -j DROP`
    - `tcpdump -ni any port 8000 -S`

---

```python
me, sport = '192.168.1.100', 10000
them, dport = '192.168.1.69', 8000
#
ip = IP(src=me, dst=them)
syn = TCP(sport=sport, dport=dport, flags='S', seq=1000)
synack = sr1(ip/syn)
ack = TCP(sport=sport, dport=dport, flags='A', seq=synack.ack, ack=synack.seq+1)
send(ip/ack)
```


---

## ARP Poison Program

`arper.py`

---

## DNS Spoofing:

https://thepacketgeek.com/scapy-p-09-scapy-and-dns/

---

## Your Job



---

## Reading


---


## Feedback please!

- tim@reachtim.com
- discord: https://discord.gg/WR23qUj

