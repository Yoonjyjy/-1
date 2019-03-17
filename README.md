# 2주차 과제 : 클라이언트가 보낸 문자열을 거꾸로 전송해주는 서버 구현
## null조 : 윤지영(2017037037)

* client.py
  * -i : 서버 아이피
  * -p : 포트 번호
  * -s : 보낼 문자열
 
* server.py
  * -p : 포트 번호
  
사진 : client.PNG와 server.PNG

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
 
 사진 : result.PNG
  
 <pre><code>assignment_1.py -o A -i 5 4 3 2 5 1 1 1 -2 -2 -3 0 -1 100 0</code></pre>
![result](https://github.com/Yoonjyjy/computerNetwork_1/blob/master/result.PNG?raw=true)
