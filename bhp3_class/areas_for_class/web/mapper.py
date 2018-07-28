import os
import queue
import requests
import sys
import threading
import time

FILTERS = [".jpg", ".gif", ".png", ".css"]
TARGET = "http://boodelyboo.com/wordpress"
THREADS = 10

web_paths = queue.Queue()
answers = queue.Queue()

def gather_paths(dirname):
    os.chdir(dirname)
    for root, dname, files in os.walk('.'):
        for fname in files:
            if os.path.splitext(fname)[1] in FILTERS:
                continue
            path = os.path.join(root, fname)
            if path.startswith('.'):
                path = path[1:]
            print(path)
            web_paths.put(path)

def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = f'{TARGET}{path}'
        time.sleep(2)
        r = requests.get(url)
        if r.status_code == 200:
            answers.put(url)
            # print(f'Found location: {url}')
    sys.exit()
            
def run():
    for i in range(THREADS):
        print(f'Spawning thread {i}')
        t = threading.Thread(target=test_remote)
        t.start()

if __name__ == '__main__':
  dirname = "/Users/jtimarnold/Downloads/wordpress"
  gather_paths(dirname)
  input('Press return to continue.')
  run()
  web_paths.join()
  print('got the paths now.')
  answerlist = list(answers.queue)
  with open('myanswers.txt', 'w') as f:
      f.writelines(answerlist)
  print('done')