# 12주차 Termproject : Traceroute 작성
## null조 : 팀 대표 윤지영(2017037037), 팀원 김도형(2013040008), 박세호(2017037022)

* traceroute.py

* 사진 : 
  * '텀프로젝트 ICMP.PNG' - icmp 실행
  * '텀프로젝트 UDP.PNG' - udp 실행
  * '텀프로젝트 ICMP 패킷.PNG' - wireshark로 icmp 실행 패킷 캡쳐
  * '텀프로젝트 UDP 패킷.PNG' - wireshark로 udp 실행 패킷 캡쳐

  실행 결과 화면 :
  
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/%ED%85%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20ICMP.PNG?raw=true)
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/%ED%85%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20UDP.PNG?raw=true)
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/%ED%85%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20ICMP%20%ED%8C%A8%ED%82%B7.PNG?raw=true)
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/%ED%85%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%20UDP%20%ED%8C%A8%ED%82%B7.PNG?raw=true)

***
***
***

# 10주차 과제 : ICMP Echo Request 패킷을 작성해서 전송하는 프로그램 작성
## null조 : 팀 대표 윤지영(2017037037), 팀원 김도형(2013040008), 박세호(2017037022)

* icmp.py
 
아직 코드는 미완성입니다!

***
***
***

# 9주차 과제 : Linux에서 IP Packet을 수신해 Ethernet 헤더, IP 헤더, 페이로드를 는 프로그램 작성
## null조 : 팀 대표 윤지영(2017037037), 팀원 김도형(2013040008), 박세호(2017037022)

* ether_sniffer.py
  
* 사진 : 
  * '9주차과제1.PNG' - ether_sniffer.py 실행 [1]
  * '9주차과제2.PNG' - ether_sniffer.py 실행 [2]
  * '9주차과제3.PNG' - ping google.com -c 1 실행

* 실험 환경 :
  * AF_PACKET을 사용하고 PROTOCOL_TYPE은 ETH_P_ALL을 사용. 
  * Ethernet 헤더 파싱 후 Ether_type을 통해 IP 패킷인지 검사 후 IP 패킷일 때만 출력
  * IP 헤더는 헤더의 길이를 먼저 구한 뒤 옵션을 제외한 길이에 맞게 파싱 
  * While 루프를 통해 여러 번 동작하도록 작성 
  * 프로그램 실행 뒤 google.com에 PING을 1번 보낸 결과를 캡쳐해 첨부
  <pre><code>python3 ether_sniffer.py –i ens33</code></pre>
  <pre><code>ping google.com -c 1</code></pre>
 
  실행 결과 화면 :
  
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/9%EC%A3%BC%EC%B0%A8%EA%B3%BC%EC%A0%9C1.PNG?raw=true)
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/9%EC%A3%BC%EC%B0%A8%EA%B3%BC%EC%A0%9C2.PNG?raw=true)
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/9%EC%A3%BC%EC%B0%A8%EA%B3%BC%EC%A0%9C3.PNG?raw=true)

***
***
***

# 8주차 과제 : raw_sniffer.py를 이용해 패킷을 분석하여 한글 파일로 정리 후 제출
## null조 : 팀 대표 윤지영(2017037037), 팀원 김도형(2013040008), 박세호(2017037022)

* raw_sniffer.py를 이용해 리눅스에서 과제2가 실행되면서 서버-클라이언트 간 주고받은 첫 번째 TCP 패킷을 캡처해 사진으로 첨부하고 패킷을 상세히 분석하여 한글 파일로 2장 내로 정리 후 제출

* 한글 파일 :
  * 컴퓨터 네트워크 8주차 과제.hwp

***
***
***

# 7주차 과제 : wireshark 프로그램에 대해서 조사한 뒤 한글 파일로 조사결과 정리 후 제출
## null조 : 팀 대표 윤지영(2017037037), 팀원 김도형(2013040008), 박세호(2017037022)

* 한글 파일 :
  * wireshark에 대하여.hwp

***
***
***

# 6주차 과제 : threading 모듈을 사용해 서버와 클라이언트가 대화를 주고 받을 수 있는 프로그램 작성
## null조 : 팀 대표 윤지영(2017037037), 팀원 김도형(2013040008), 박세호(2017037022)

* talk_client.py
  * -i : 서버 아이피
  * -p : 포트 번호
 
* talk_server.py
  * -p : 포트 번호
  
* 사진 : 
  * '서버 캡쳐.PNG'
  * '클라이언트 캡쳐.PNG'


* 실험 환경 :
  * 서버는 클라이언트가 전송한 문자열 출력, input()으로 사용자 입력을 받아서 클라이언트에 전달
  * 클라이언트는 서버가 전송한 문자열 출력, input()으로 사용자 입력을 받아서 서버에 전달
  * 각각의 쉘에서 talk_server.py와 talk_client.py 켜기!
  * 난이도 조절을 위해 서버는 1개의 클라이언트만 처리
  <pre><code>python talk_server.py –p 8888</code></pre>
  <pre><code>python talk_client.py –p 8888 –i 127.0.0.1 </code></pre>
 
  실행 결과 화면(위가 서버 실행, 아래가 클라이언트 실행) :
  
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/%EC%84%9C%EB%B2%84%20%EC%BA%A1%EC%B3%90.PNG?raw=true)
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/%ED%81%B4%EB%9D%BC%EC%9D%B4%EC%96%B8%ED%8A%B8%20%EC%BA%A1%EC%B2%98.PNG?raw=true)

***
***
***

# 5주차 과제 : threading 모듈을 사용해 다수의 client의 요청을 받을 수 있는 서버 작성 
## null조 : 팀 대표 윤지영(2017037037), 팀원 김도형(2013040008), 박세호(2017037022)

* thread_client.py
  * -i : 서버 아이피
  * -p : 포트 번호
 
* thread_server.py
  * -p : 포트 번호
  
* 사진 : 
  * '실행 결과_5주차.PNG'

* 실험 환경 :

  * 각각의 쉘에서 thread_server.py와 thread_client.py 켜기!
  * (클라이언트는 다수의 요청을 받을 수 있는지 알아야 하므로 여러 창을 띄워 실행해야 하며 테스트의 경우 두 창을 띄움)
  <pre><code>python thread_server.py –p 8888</code></pre>
  <pre><code>python thread_client.py –p 8888 –i 127.0.0.1 </code></pre>
  <pre><code>python thread_client.py –p 8888 –i 127.0.0.1 </code></pre>
  
  * 각각의 클라이언트가 다른 입력값을 넣으면 각자 뒤집은 문자열을 받을 수 있음
 
  실행 결과 화면(위가 서버 실행, 아래 두 개가 클라이언트 실행) :
  
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/%EC%8B%A4%ED%96%89%EA%B2%B0%EA%B3%BC_5%EC%A3%BC%EC%B0%A8.PNG?raw=true)

***
***
***

# 4주차 과제 : 한글 파일로 조사결과 정리 후 제출

***
***
***

# 3주차 과제 : 클라이언트가 요청한 파일을 전송해주는 서버 구현
## null조 : 팀 대표 윤지영(2017037037), 팀원 김도형(2013040008), 박세호(2017037022)

* client2.py
  * -i : 서버 아이피
  * -p : 포트 번호
  * -f : 파일 이름
 
* server2.py
  * -p : 포트 번호
  * -d : 파일 디렉토리
  
* 사진 : 
  * 'net3폴더.PNG'
  * '실행 결과(server2.py, client2.py).PNG'
  * '전송 전 새 폴더.PNG'
  * '전송 후 새 폴더.PNG'

* 텍스트 파일 : test.txt(전송할 테스트 파일)

* 실험 환경 :
  * 찾을 파일을 둔 디렉토리 주소 : /Python/computerNetwork/computerNetwork_3
  * server2.py와 client2.py를 넣어둔 디렉토리 주소 : C:\Users\윤지영\Desktop\새 폴더
  * 찾을 파일의 이름 : test.txt
  * 찾은 파일의 내용 : Hello world!

  각각의 쉘에서 client2.py와 server2.py 실행 !
  <pre><code>python server2.py -p 8888 -d /Python/computerNetwork/computerNetwork_3</code></pre>
  <pre><code>python client2.py -i 127.0.0.1 -p 8888 -f "test.txt"</code></pre>
  
  * 전송하는 요소가 많아 헷갈릴 것을 우려해 전송내용 1 ~ 5의 식으로 주석을 추가하였음
  * client2.py의 전송내용 1과 server2.py의 전송내용 1이 대응됨
 
  computerNetwork_3의 내용 : 
  
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/net3폴더.PNG?raw=true)

  전송 전 새 폴더의 내용 : 
  
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/%EC%A0%84%EC%86%A1%20%EC%A0%84%20%EC%83%88%20%ED%8F%B4%EB%8D%94.PNG?raw=true)

  실행 결과 화면(위가 서버 실행, 아래가 클라이언트 실행) :
  
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/%EC%8B%A4%ED%96%89%20%EA%B2%B0%EA%B3%BC(server2.py,%20client2.py).PNG?raw=true)

  전송 후 새 폴더의 내용 :
  
  ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/%EC%A0%84%EC%86%A1%20%ED%9B%84%20%EC%83%88%20%ED%8F%B4%EB%8D%94.PNG?raw=true)

***
***
***

# 2주차 과제 : 클라이언트가 보낸 문자열을 거꾸로 전송해주는 서버 구현
## null조 : 윤지영(2017037037)

* client.py
  * -i : 서버 아이피
  * -p : 포트 번호
  * -s : 보낼 문자열
 
* server.py
  * -p : 포트 번호
  
* 사진 : 
  * 'client.PNG'
  * 'server.PNG'

 각각의 쉘에서 client.py와 server.py 실행 !
 <pre><code>python client.py -i 127.0.0.1 -p 8888 -s string</p>:(거꾸로 전송할 문자열)</code></pre>
 <pre><code>python server.py -p 8888</code></pre>
 ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/client.PNG?raw=true)
 ![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/server.PNG?raw=true)

***
***
***

# 1주차 과제 : Python을 이용한 Quick sort (컴퓨터 네트워크)
## null조 : 윤지영(2017037037)

* assignment_1.py
  * -o : 정렬 방식을 정하는 옵션 (A->오름차순, D->내림차순)
  * -i : 뒤에 오는 것이 정렬할 배열
  
처음 -o 가 제대로 입력되지 않았을 때
 -> "정렬 방식 옵션을 다시 입력해 주십시오." 출력
 
-o 뒤에 'A'나 'D' 중 하나로 입력되지 않았을 때
 -> "정렬 옵션은 'A'나 'D'중 하나로 입력해 주십시오." 출력
 
* 사진 : result.PNG
  
 <pre><code>assignment_1.py -o A -i 5 4 3 2 5 1 1 1 -2 -2 -3 0 -1 100 0</code></pre>
![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/result.PNG?raw=true)
