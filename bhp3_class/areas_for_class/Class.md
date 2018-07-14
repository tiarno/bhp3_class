
## Welcome to class!

### Black Hat Python3 

### Raleigh ISSA

---

## Introductions

---

## Logistics 1

- Web class Wednesdays 7:00 - 8:30 EDT
- Interaction during class
- Discord Channel to help each other
https://discord.gg/GCrC94

- Discord Office Hour Monday, 7:00 - 8:00
- Direct message on Discord or email: tim@reachtim.com

---

## Logistics 2

- GitHub Repo of class materials/updated code
  https://github.com/tiarno/bhp3_class

- Based on Black Hat Python by Jason Seitz. 
    - Recommended, not required. 
    - https://www.amazon.com/Black-Hat-Python-Programming-Pentesters/dp/1593275900


---

## Pilot class: Interaction

- Need class interaction
    - use your microphone during class
    - use chat during class
    - use the Discord chat after class

---

## Pilot class: Feedback

- Need feedback:
    - class length
    - class frequency
    - class speed
    - subjects of interest

---

## Structure of the repo

This repo is structured as follows::

    bhp3_class/
        Install.md
        README.md
        setup.py
        bhp3_class/
          __init__.py
          networking/
          packets/
          web/

          areas_for_class/
            Class.md
            demo_plus/
            networking/
            packets/
            web/

---

## Every class we'll have updates:

```python
        areas_for_class/
            Class.md
            demo_plus/
            networking/
            packets/
            web/
```

---

## Syllabus

Class will cover chapters 2, 3, 4, and 5 of 
the book Black Hat Python. We'll follow this order:

-  `web`
-  `networking`
-  `packets`

---

## What you need to have

- Linux OS (I'm using Kali and Mac)
- Python 3.x (I'm using Python 3.6)
- IDE or text editor (I'm using VSCode)

---

## What you need to know

- Not a beginner's class, that's coming.
- Get 70% or better average on these areas from this location: https://www.programiz.com/python-programming/quiz

    - Introduction
    - Object and Class
    - Native Data Types
    - Files and Exceptions
    - Functions

---

## Optional 

Use the installation instructions at the top
level if you want help to install a Kali VM 
in VirtualBox and the VSCode IDE.

---

## Git notes

- Never push creds
- Use your .gitignore file
- push often
- code with pep8

---

## Virtualenvs and `pipenv`

<span style="color:red">Activity</script>

- Install the github repo
    - https://github.com/tiarno/bhp3_class
    - download or clone

- `apt-get install -y python3-pip`
- `pip3 install pipenv`

- cd into `bhp3_class`

---

## Install Dependencies

<span style="color:red">Activity</script>

- pipenv install scapy
- pipenv install lxml
- pipenv install requests
- pipenv install paramiko
- pipenv install pylint
- pipenv install -e .

---

# Start a Python process

<span style="color:red">Activity</script>

`pipenv shell`

```python
Python 3.6.3 (default, Oct  3 2017, 21:16:13) 
[GCC 7.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import scapy
>>>```


---

## Download WordPress

<span style="color:red">Activity</script>

https://wordpress.org/latest.tar.gz

We'll use this later on in this part of the class.

---

## os.walk

<span style="color:lightblue">Demo</script>

<span style="color:red">Activity</script>

---

## Code Hygiene and `pep8`

- `__main__`
- import order
- variable names
- encapsulate functionality
- avoid globals

---

## Lists, Queues, and Dequeues

<span style="color:lightblue">Demo</script>

- `mylist.append()` 
- `mylist.pop()`

![listimage](./images/rrm52.png)


---

<span style="color:lightblue">Demo</script>

- `myqueue.put()` 
- `myqueue.get()`

![queueimage](./images/phzXA.jpg)

- `mydequeue.append()`
- `mydequeue.popleft()`
- `mydequeue.pop()`

---

## timeit is your friend!

    $ python -mtimeit -s'q=range(10000)' 'q.append(23); q.pop(0)'

    100000 loops, best of 3: 5.81 usec per loop


    $ python -mtimeit -s'import collections; q=collections.deque(range(10000))' 'q.append(23); q.popleft()'

    1000000 loops, best of 3: 0.574 usec per loop

---

## Classes and Functions

- incline toward functions

- If you find yourself passing data
structures among functions, think about a class.



---

## The `requests` Module

http://docs.python-requests.org/en/master/

---

## Threads vs Processes

<span style="color:lightblue">Demo</script>

Multithreading is for responsive apps. 

Multiprocessing is for parallelism.

---

## `enumeration with mapper.py` 

<span style="color:lightblue">Demo</script>

<span style="color:red">Activity</script>

---

## Kali Wordlists

<span style="color:lightblue">Demo</script>

<span style="color:red">Activity</script>

```user@kali:/usr/share/wordlists ```

---

## `enumeration with dirfinder.py`

<span style="color:lightblue">Demo</script>

<span style="color:red">Activity</script>

---

## `BytesIO`

https://webkul.com/blog/using-io-for-creating-file-object/

---

## Browser Dev Tools

<span style="color:lightblue">Demo</script>

<span style="color:red">Activity</script>

http://boodelyboo.com/wordpress


---

## `lxml` module and Xpath

```python
    parser = etree.HTMLParser()
    tree = etree.parse(BytesIO(content), parser=parser)
    for elem in tree.findall('//input'):
        # do stuff with elem

```


---

## `wp_killer.py`

<span style="color:lightblue">Demo</script>

---

## Summary 1

- Feedback
- Python, Linux, Dependencies
- pipenv

---

# Summary 2

- `os.walk`
- threading
- mapping an app
- word lists for enumeration
- word lists for password bruteforce
- browser tools
- `lxml` for web parsing

---

## Reading

- BHP, Chapter 5 (web hacking)

- Requests http://docs.python-requests.org/en/master/

- `BytesIO` https://webkul.com/blog/using-io-for-creating-file-object/

---

## Your Job

- populate your bhp3_class module
    - mapper.py
    - dirfinder.py

---

## Pick your app

https://www.capterra.com/content-management-software/

https://www.makeuseof.com/tag/10-popular-content-management-systems-online/

Put your new code into the `web` module

---