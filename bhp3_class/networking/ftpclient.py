from ftplib import FTP
from getpass import getpass
from pprint import pprint
import sys
import time

def connect(host, port, user, password):
    print(host, port)
    print('begin')
    myconn = FTP()
    print(myconn)
    myconn.connect(host, port)
    print('got the connection, logging in...')
    myconn.login(user, password)
    
    pprint(myconn.nlst())
    time.sleep(5)

if __name__ == '__main__':
    if len(sys.argv) == 4:
        host = sys.argv[1]
        port = int(sys.argv[2])
        user = sys.argv[3]
        passwd = getpass()
        connect(host, port, user, passwd)
    else:
        print('Usage: host port user passwd')
    
