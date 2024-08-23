import os
import socket
import time




def send_file():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 9999))

    file_name = input('Enter file name: ')

    file = open(f'send/{file_name}', 'rb')
    file_size = os.path.getsize(f'send/{file_name}')
    file_size = str(file_size)

    client.send('received.png'.encode())
    client.send(file_size.encode())
    time.sleep(0.1)
    data = file.read()
    client.sendall(data)
    client.send(b'<FILE_FINISHED>')

    file.close()
    client.close()


# simple cli
print('Sender')
print('1. Send file')
print('2. Exit')
choice = input('Enter choice: ')
if choice == '1':
    send_file()
elif choice == '2':
    print('Exiting...')
    exit()