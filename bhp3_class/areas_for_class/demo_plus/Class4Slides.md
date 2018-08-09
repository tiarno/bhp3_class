## Welcome to class 4!

### Black Hat Python3 

### Raleigh ISSA

---

## Github repo

https://github.com/tiarno/bhp3_class

---

## Summary from last class

- Joining threads (blocking)
- Briefly, context managers (`with ...`)
- lxml for web scraping
- sockets
- IP, ICMP headers and parsing

---

## UDP Scanner

- how it works
- UDP packet to unused port
    - network unreachable (from router)
    - host unreachable (from router)
    - port unreachable **!** type 3, code 3

---

## Test it out

- `scanner.py`

---

## Python details

- git
- imports
- ipaddress
- bytes/strings
- context managers

---

## Git Local

Plain Git:

- add
- commit 
- status
- git log --pretty=oneline

---

## Git and GitHub

- git fork is a GitHub thing only
- `git clone` (get a copy of a repo)
- git and your local repo:
    - add/commit changes
    - can have a remote (e.g., GitHub)
    - git pull (pulls down updates from the remote)
    - git push (pushes up changes to the remote of your repo)

    - can have an upstream (from the original fork: a GitHub thing)

---

## imports

- `__init__.py`
- import os -> os.path, os.listdir()
- from lxml import etree -> etree.parse()
- import multiprocessing as mp -> mp.Process()
- from ctypes import * -> Structure

---

## word finder function

### Code reuse!

- `bhp3_class/web/__init__.py` -> getwords()
- `dirfinder2.py`
- `wp_killer2.py`

---

## `ipaddress` package

```python
  IPv4Network('192.168.1.69/16')
    .hosts() -> iterator over usable hosts in network

  ipaddress.ip_address(self.src)
```

---

## Network Scanner code:

scanner.py
```
for ip in ipaddress.ip_network(SUBNET).hosts():
    send packet to ip
```

---

## Bytes vs Strings

- sockets, processes return bytes
- bytes are the computer's language
- strings are our language
- string.encode() -> bytes
- bytes.decode() -> string

Usually the decoding is to a UTF-8 string

---

```
S.encode(encoding='utf-8', errors='strict') -> bytes
    Encode S using the codec registered for encoding. 

B.decode(encoding='utf-8', errors='strict') -> string
    Decode the bytes using the codec registered for encoding.
```

Default encoding is 'utf-8'

---

## Context Managers

- As a class, define `__enter__` and `__exit__`
- As a generator (`try: finally:`)
    - code before the `yield` == `__enter__`
    - code in the `finally` block is the `__exit__`

---

```
@contextmanager
def some_generator(<arguments>):
    <setup>
    try:
        yield <value>
    finally:
        <cleanup>
```

So that

```
with some_generator(<arguments>) as <variable>:
   <body>

```

is 
equivalent to this:

```
<setup>
try:
   <variable> = <value>
   <body>
finally:
    <cleanup>
```

---

- Can use `contextlib.contextmanager` decorator
- Built in context managers (e. g., files, sockets)
- closing, redirect_stdout, see doc for more...

---

```
with closing(<module>.open(<arguments>)) as f:
    <block>
```
is equivalent to this:

```
f = <module>.open(<arguments>)
try:
    <block>
finally:
    f.close()
```

---

## `redirect_stdout`

How to write help() to a file


```
with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)
```

---

## Your Job

- Write your own network scanner, place it in `packets` module
- Read about context managers
- Become familiar with bytes vs strings, encoding vs decoding.

---

## Feedback please!

- tim@reachtim.com
- discord: https://discord.gg/WR23qUj

---

## Extra links

- https://www.securitywizardry.com/index.php/tools/packet-headers.html
- https://stackoverflow.com/questions/9257533/what-is-the-difference-between-origin-and-upstream-on-github/9257901#9257901

- http://ndpsoftware.com/git-cheatsheet.html#loc=remote_repo;