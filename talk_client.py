#talk_client.py

import socket
import threading
import argparse

parser = argparse.ArgumentParser(description="Echo client -p port -i host")
parser.add_argument('-p', help = "port_number", required = True)
parser.add_argument('-i', help = "host_name", required = True)
args = parser.parse_args()

host = args.i
port = int(args.p)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def recv():
    while True:
        try:
            data = s.recv(1024)
            if not data:
                continue
            print(data.decode())
        except:
            pass

def send():
    while True:
        data = input()
        data = data.encode()
        s.send(data)

threading._start_new_thread(send, ())
threading._start_new_thread(recv, ())

while True:
    pass