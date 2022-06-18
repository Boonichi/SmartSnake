import socket
import struct
import traceback
import logging
import time

HOST = '127.0.0.1'
PORT = 63420
message = 'snake'
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen(1)
        conn, addr = s.accept()
        conn.send(b"1,2,3")
        msg = "hello"
        conn.send(msg.encode())
