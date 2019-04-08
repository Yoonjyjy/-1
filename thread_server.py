# thread_server.py

import socket
import threading
import argparse


def socket_handler():
    while True:
            
        data=conn.recv(1024)
        data = data.decode()
        data=data[::-1]
        conn.sendall(data.encode())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Thread server -p port")
    parser.add_argument('-p', help = "port_number", required = True)

    args = parser.parse_args()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', int(args.p)))
    server.listen(5)

    while True:
        conn, addr = server.accept()
        threading._start_new_thread(socket_handler,())

    server.close()