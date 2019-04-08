# thread_client.py

import socket
import argparse

def run(host,port):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.connect((host, port))
      line = input('문자 입력 : ')
      s.sendall(line.encode())
      receive=s.recv(1024)
      print("서버로 부터 받은 문자열 : " , receive.decode())

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Echo client -p port -i host")
  parser.add_argument('-p', help="port_number", required=True)
  parser.add_argument('-i', help="host_name", required=True)
  args = parser.parse_args()
  run(host=args.i, port=int(args.p))