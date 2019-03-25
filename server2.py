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
        msg = conn.recv(1024)   ## 파일 이름을 받아옴(*전달내용 1*)
        print("file name : " + msg.decode()) ## 'file name : (파일 이름)'으로 출력
        
        if os.path.isfile(sys.argv[4]+'/'+msg.decode()): ## 지정한 경로에 원하는 파일이 있는지 검사
                conn.sendall("OK".encode())     ## *전달내용 2-1*, 파일이 있을 경우 OK 사인을 보내줌 
                file_size = os.path.getsize(sys.argv[4]+'/'+msg.decode()) ## 파일의 크기를 구해 저장
                print("size : "+str(file_size)) ## 'size : (파일 크기)'로 출력
                conn.sendall(str(file_size).encode()) ## *전달내용 3*, 파일의 크기를 전송
                resp = conn.recv(2) ## *전달내용 4*, OK 사인을 받음

                filename = sys.argv[4]+'/'+msg.decode() ## 파일을 읽기 위해 filename에 파일의 주소와 파일 이름을 합해 저장
                file = open(filename, 'rb') ## 파일을 읽음
                text_str = file.read(file_size) ## text_str에 아까 구한 파일의 사이즈만큼 파일을 읽어 저장
                file.close() ## 파일 닫기

                conn.sendall(text_str) ## *전달내용 5*, 저장한 파일의 내용들을 전송

        else :                                  ## 지정했던 경로에 원하는 파일이 없을 경우 -1을 보내줌
                conn.sendall("-1".encode())     ## *전달내용 2-2*

        conn.sendall(msg)
        conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo server -p port -d directory")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-d', help="file_directory", required=True)


    args = parser.parse_args()
    run_server(port=int(args.p))
