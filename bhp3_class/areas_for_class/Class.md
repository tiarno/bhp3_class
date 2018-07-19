
## Welcome to class 2!

### Black Hat Python3 

### Raleigh ISSA

---

## Logistics

- Web class Wednesdays 7:00 - 8:30 EDT
- Interaction during class
- Discord Channel to help each other
https://discord.gg/WR23qUj

- Discord Office Hour Monday, 7:00 - 8:00
- Direct message on Discord or email: tim@reachtim.com

- GitHub Repo of class materials/updated code
  https://github.com/tiarno/bhp3_class

---

# Summary from last class

- `os.walk`
- lists, queues, deques
- threading

---

# Let's Code!

- Target website uses a popular framework.
- enumerate that website for further attacks.

---

## `enumeration with mapper.py` 

<span style="color:lightblue">Demo</script>

---

# Let's Code!

- Target website uses an unknown architecture.
- enumerate that website for further attacks.

---

## Kali Wordlists

<span style="color:lightblue">Demo</script>

<span style="color:red">Activity</script>

```user@kali:/usr/share/wordlists ```

---

## `enumeration with dirfinder.py`

<span style="color:lightblue">Demo</script>

---

# Let's Code!

- Target website is WordPress.
- Brute force the login page.

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
    1. parser = etree.HTMLParser()
    2. tree = etree.parse(BytesIO(content), parser=parser)
    3. for elem in tree.findall('//input'):
          # do stuff with elem

```

---

## `wp_killer.py`

<span style="color:lightblue">Demo</script>

---

# Summary 

- mapping an app
- word lists for enumeration
- word lists for password bruteforce
- browser tools
- `lxml` for web parsing

---

## Reading 1

- BHP, Chapter 5 (web hacking)

- GitHub Repo: https://github.com/tiarno/bhp3_class

- PEP-8: https://www.datacamp.com/community/tutorials/pep8-tutorial-python-code

---

## Reading 2

- Requests http://docs.python-requests.org/en/master/

- Threading: https://docs.python.org/3.6/library/threading.html

- `BytesIO` https://webkul.com/blog/using-io-for-creating-file-object/

---

## Your Job

- populate your `bhp3_class/web` module
    - mapper.py
    - dirfinder.py

- Can you create a function to return words from a word list?
  That would let us simplify the dirfinder/wp_killer code.

---

## Pick your app

https://www.capterra.com/content-management-software/

https://www.makeuseof.com/tag/10-popular-content-management-systems-online/

---
