#talk_server.py

import socket
import threading
import argparse

parser = argparse.ArgumentParser(description="Thread server -p port")
parser.add_argument('-p', help = "port_number", required = True)
args = parser.parse_args()

host = '127.0.0.1'
port =  int(args.p) 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept() 
print(addr[0],' ',addr[1]) 

data = "입력"
conn.send(data.encode())

def send():
    while True:
        data = input()
        data = '[server] : ' + data
        data = data.encode()
        conn.send(data)


def recv():
    while True:
        data = conn.recv(1024)
        if not data: 
            continue
        else :
            data = data.decode()
            print('[client] : ' + data)


threading._start_new_thread(send, ())
threading._start_new_thread(recv, ())

while True: 
        pass