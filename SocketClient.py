import socket

HOST = '127.0.0.1'
PORT = 63421
message = 'Sent'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(message.encode('utf-8'))
    data = s.recv(1024)

print('Received', repr(data.decode()))