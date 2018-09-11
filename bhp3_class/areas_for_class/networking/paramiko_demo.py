from getpass import getpass
import base64
import paramiko

def do_client(server_ip, user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    client.connect(server_ip, username=user, password=passwd)
    data_buffer = b''
    stdin, stdout, stderr = client.exec_command('ls -la\n')
    while not stdout.channel.exit_status_ready():
        data_buffer += stdout.channel.recv(1024)  
    print(data_buffer.decode())
    client.close()

if __name__ == '__main__':
    server_ip = '192.168.1.108'
    user = 'testuser'
    passwd = getpass()
    do_client(server_ip, user, passwd)
