#!/usr/bin/env python3

import socket

HOST = '127.0.0.2'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Received', repr(data))
            #conn.sendall(data)
            conn.sendall(b"Thank you for connection! :) - Server will disconnect now")
