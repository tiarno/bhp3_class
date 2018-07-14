import multiprocessing
import os
import pdb
import sys
import threading

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fib(n-1) + fib(n-2))

def demo(name='fib_thread'):
    if name == 'fib_thread':
        # http://www.dabeaz.com/GIL/gilvis/fourthread.html
        for i in range(10):
            n = 35
            print(f'Starting Job {i}')
            t = threading.Thread(target=fib, args=(n,))
            t.start()
           
    elif name == 'fib_mp':
        for i in range(10):
            n = 35
            print(f'Starting Job {i}')
            t = multiprocessing.Process(target=fib, args=(n,))
            t.start()
    elif name == 'walk':
        dirname = '/Users/jtimarnold/code/plastex/unittests'
        for root, dirs, files in os.walk(dirname):
            print(f'\nroot is {root}')
            print(f'  containing these dirs {dirs}')
            print(f'       and these files {files}')
    elif name == 'debug':
        j = 0
        k = 0
        pdb.set_trace()
        for i in range(10):
            j = i**2
            k = i**3
            print(f'j is {j}, k is {k}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == 'fib_thread':
            demo('fib_thread')
        elif sys.argv[1] == 'fib_mp':
            demo('fib_mp')
        elif sys.argv[1] == 'walk':
            demo('walk')
        elif sys.argv[1] == 'debug':
            demo('debug')
    else:
        for i in range(10):
            print(fib(i))
    