## client.py
import os
import socket
import argparse


def run(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        line = input("file name : ")
        s.sendall(line.encode())
        sign = s.recv(2)

        if str(sign.decode()) != "-1" :
            size = s.recv(1024)
            size = size.decode()
            print("size : " + size)
            s.sendall('OK'.encode())

            txt_str = s.recv(int(size))
            ##print(str(txt_str.decode()))

            file = open(line, 'wb')
            file.write(txt_str)
            file.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host -f file")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-i', help="host_name", required=True)
    parser.add_argument('-f', help="file_name", required=False)

    args = parser.parse_args()
    run(host=args.i, port=int(args.p))
