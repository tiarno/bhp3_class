## Welcome to class 8!

### Black Hat Python3 

### Raleigh ISSA

---

## Github repo

https://github.com/tiarno/bhp3_class

---

## Summary from last class

- building images from packet capture streams
- tcp/udp clients and servers
- starting a pure-python netcat clone

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

- Finish out your `netcat.py`


---

## Reading

- 

---

## Feedback please!

- tim@reachtim.com
- discord: https://discord.gg/WR23qUj

 