import queue
import threading
import os
import requests

THREADS = 10
TARGET    = "http://boodelyboo.com/wordpress/"
FILTERS   = [".jpg", ".gif", "png", ".css"]

web_paths = queue.Queue()

def gather_paths(dirname):
    os.chdir(dirname)
    for root, _, files in os.walk('.'):
        for fname in files:
            path = os.path.join(root, fname)
            if os.path.splitext(fname)[1] not in FILTERS:
                if path.startswith('.'):
                    path = path[1:]
                print(path)
                web_paths.put(path)

def test_remote():
    while not web_paths.empty():
        path = web_paths.get()
        url = f'{TARGET}{path}'
        r = requests.get(url)
        if r.status_code == 200:
            print(f'Found location: {url}')
            
def run():
    for i in range(THREADS):
        print(f'Spawning thread {i}')
        t = threading.Thread(target=test_remote)
        t.start()

if __name__ == '__main__':
  dirname = "/Users/jtimarnold/Downloads/wordpress"
  gather_paths(dirname)
  run()
