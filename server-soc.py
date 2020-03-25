#!/usr/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 65432       # Port to listen on ( non-privilege ports > 1023 )

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f'Connnected by {addr}')
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            conn.sendall(b'Hello, from server') # send data to client
            print(data)
            s.close();
