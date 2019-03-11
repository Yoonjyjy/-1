import sys

def quick(list):                # 퀵 정렬 함수 생성
    if len(list)<=1 :           # 정렬할 데이터가 2 미만(1개)이면 그대로 출력
        return list
    else :
        pivot = list[len(list)//2]  # 피벗은 리스트의 가운데 값으로 지정
        left = []
        right = []
        mid = []                # 세 개의 배열 생성
        if option == 'A' :      # A는 오름차순으로 정렬
            for data in list :  # 피벗보다 작으면 left, 크면 right, 그 외(동일한 경우)는 mid로 집어넣기
                if data < pivot :
                    left.append(data)
                elif data > pivot :
                    right.append(data)
                else :
                    mid.append(data)
        elif option == 'D' :    # D는 내림차순으로 정렬
            for data in list :
                if data < pivot :       # 아까와 반대로 피벗보다 작으면 right로 보내기
                    right.append(data)
                elif data > pivot :     # 피벗보다 크면 left로 보내기
                    left.append(data)
                else :
                    mid.append(data)
        return quick(left) + mid + quick(right)
    
##################

length = len(sys.argv) - 1      # length에 명령행 인자의 길이를 저장하되 리스트는 0부터 시작이므로 -1을 해줌
list = []                       # 정렬할 데이터들을 넣을 리스트 생성

if sys.argv[3]=='-i':           # -i이 맞으면 그 다음인 sys.argv[4]부터 length번째 인자까지 리스트에 넣기
    now = 4                     # 리스트에 어디까지 넣었는지 확인하기 위한 변수 now
    while (now <= length) :
        list.append(int(sys.argv[now]))  # 리스트에 값 추가, sys.argv[now]는 str이므로 정렬을 위해 int형으로 변환해줌
        now += 1

if sys.argv[1]=='-o':           # -o는 정렬 방식 옵션
    if sys.argv[2]=='A':        # A는 오름차순 정렬
        option = 'A'
        print(quick(list))
    elif sys.argv[2]=='D':      # D는 내림차순 정렬
        option = 'D'
        print(quick(list))
    else:                       # A나 D가 아닌 다른 글자가 들어갔을 경우
        print("정렬 옵션은 'A'나 'D'중 하나로 입력해주십시오.")
else :
    print("정렬 방식 옵션을 다시 입력해 주십시오.")
