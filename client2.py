## client.py
import os
import socket
import argparse


def run(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        line = input("file name : ")
        s.sendall(line.encode())    ## *전달내용 1*
        sign = s.recv(2)            ## *전달내용 2*, 경로에 파일이 있는지 검사한 결과로 OK나 -1을 받음

        if str(sign.decode()) != "-1" : ## 경로에 파일이 없는 경우가 아니면(=있으면) 실행, 파일이 없으면 종료
            size = s.recv(1024) ## *전달내용 3*, 파일의 크기를 전달받음
            size = size.decode()
            print("size : " + size) ## 'size : (파일 크기)'로 출력해줌
            s.sendall('OK'.encode()) ## *전달내용 4*, 사이즈를 전달받고 OK 전송

            txt_str = s.recv(int(size)) ## *전달내용 5*, 아까 전달받은 사이즈만큼만 txt_str에 전달받음

            file = open(line, 'wb') ## line(맨 처음 입력받은 파일 이름)을 이용해 똑같은 이름의 파일 쓰기
            file.write(txt_str) ## 그 안에 txt_str(전달받은 파일 내용물)을 작성
            file.close() ## 파일 닫기


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Echo client -p port -i host -f file")
    parser.add_argument('-p', help="port_number", required=True)
    parser.add_argument('-i', help="host_name", required=True)
    parser.add_argument('-f', help="file_name", required=False)

    args = parser.parse_args()
    run(host=args.i, port=int(args.p))
