from bhp3_class.web import getwords
import queue
import requests
import threading

AGENT = "Mozilla/5.0 (X11; Linux x86_64; rv:19.0) Gecko/20100101 Firefox/19.0"
EXTENSIONS = ['.php', '.bak', '.orig', '.inc']
TARGET = "http://testphp.vulnweb.com"
THREADS = 50
WORDLIST = "/mydownloads/all.txt" # See SVNDIGGER

def extend_words(words):
    allwords = queue.Queue(words)
    for word in words:
        if "." in word:
            allwords.put(f'/{word}')
        else:
            allwords.put(f'/{word}/')

        for extension in EXTENSIONS:
            allwords.put(f'/{word}{extension}')
    return allwords

def dir_find(words):
    while not words.empty():
        word = words.get()
        url = f'{TARGET}{word}'
        headers = {'User-Agent': AGENT}
        try:
            r = requests.get(url, headers=headers)
        except requests.exceptions.ConnectionError:
            print('x', end='')
            continue

        if r.status_code != 200:
            if r.status_code == 404:
                print('.', end='')
            else:
                print(f'{r.status_code} => {url}')
        else:
            print(f'\nSuccess ({r.status_code}: {url})')

if __name__ == '__main__':
    # getwords returns list
    # extend_words returns queue
    words = extend_words(get_words(WORDLIST))
    for _ in range(THREADS):
        t = threading.Thread(target=dir_find, args=(words,))
        t.start()
