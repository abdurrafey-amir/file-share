import os
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 9999))


file = open('send/player.png', 'rb')
file_size = os.path.getsize('send/player.png')
file_size = str(file_size)

client.send('received.png'.encode())
client.send(file_size.encode())
time.sleep(0.1)
data = file.read()
client.sendall(data)
client.send(b'<FILE_FINISHED>')

file.close()
client.close()