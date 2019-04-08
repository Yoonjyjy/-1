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

  각각의 쉘에서 thread_server.py와 thread_client.py 켜기!
  (클라이언트는 다수의 요청을 받을 수 있는지 알아야 하므로 여러 창을 띄워 실행해야 하며 테스트의 경우 두 창을 띄움)
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
