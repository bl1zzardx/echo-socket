#!/usr/bin/env python3

import socket
import subprocess

def my_Popen():
    process = subprocess.Popen("lscpu", stdout=subprocess.PIPE)
    out, err = process.communicate()
    return out

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b'free text')
    s.sendall( my_Popen() )
    data = s.recv(1024)

print('Received', repr(data))