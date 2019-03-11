import sys

def quick(list):            # 퀵 정렬 함수 생성
    if len(list)<=1 :         # 정렬할 데이터가 2 미만(1개)이면 그대로 출력
        return list
    elif option == 'A' :
        pivot = list[len(list)//2]  # 피벗은 리스트의 가운데 값으로 지정
        left = []
        right = []
        mid = []                # 세 개의 배열 생성
        for data in list :
            if data < pivot :
                left.append(data)
            elif data > pivot :
                right.append(data)
            else :
                mid.append(data)
        return quick(left) + mid + quick(right)
    elif option == 'D' :
        pivot = list[len(list)//2]
        left = []
        right = []
        mid = []
        for data in list :
            if data < pivot :
                right.append(data)
            elif data > pivot :
                left.append(data)
            else :
                mid.append(data)
        return quick(left) + mid + quick(right)

##################

length = len(sys.argv) - 1      # length에 명령행 인자의 길이를 저장하되 리스트는 0부터 시작이므로 -1
#print(length)
list = []                       # 정렬할 데이터들을 넣을 리스트 생성

if sys.argv[3]=='-i':           # -i이 맞으면 그 다음인 sys.argv[4]부터 len(sys.argv)번째 인자까지만 리스트에 넣기
    now = 4                     # 리스트에 어디까지 넣었는지 확인하기 위한 변수 now
    while (now <= length) :
        list.append(int(sys.argv[now]))  # 리스트에 값 추가
        now += 1

#print(list)

if sys.argv[1]=='-o':           # -o는 정렬 방식 옵션
    if sys.argv[2]=='A':        # A는 오름차순 정렬
        option = 'A'
        print(quick(list))
        #print("오름차순 정렬")
    elif sys.argv[2]=='D':      # D는 내림차순 정렬
        option = 'D'
        print(quick(list))
        #print("내림차순 정렬")
    else:                       # A나 D가 아닌 다른 글자가 들어갔을 경우
        print("정렬 옵션은 'A'나 'D'중 하나로 입력해주십시오.")
else :
    print("정렬 방식 옵션을 다시 입력해 주십시오.")



#####################



