## server.py
import os
import socket
import argparse
import sys


def run_server(port=4000):
    host = '' ## 127.0.0.1 Loopback

    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1) ## max 1 client

        conn, addr = s.accept()
        msg = conn.recv(1024)
        print("file name : " + msg.decode())
        
        if os.path.isfile(sys.argv[4]+'/'+msg.decode()):
                conn.sendall("OK".encode())
                file_size = os.path.getsize(sys.argv[4]+'/'+msg.decode())
                print("size : "+str(file_size))
                conn.sendall(str(file_size).encode())
                resp = conn.recv(2)

                filename = sys.argv[4]+'/'+msg.decode()
                file = open(filename, 'rb')
                text_str = file.read(file_size)
                ## print(text_str)
                file.close()

                conn.sendall(text_str)
        else :
                conn.sendall("-1".encode())

        conn.sendall(msg)
        conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo server -p port -d directory")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-d', help="file_directory", required=True)


    args = parser.parse_args()
    run_server(port=int(args.p))