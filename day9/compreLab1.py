"""
[ 실습 1 ]
1. 파일명 : compreLab1.py
2. 구현해야 하는 함수 사양
   함수명 : createList
   매개변수 : 0개 이상의 위치(포지션) 아규먼트를 받는 매개변수 1개  --> 가변인수
             기본값이 있는 매개변수 1개(매개변수 명은 type이며 기본값은 1이다.)
   리턴값 : 1개
   기능 :
  0개 이상의 위치 아규먼트를 가지고 아래에 제시된 타입에 따른 리스트를 생성하여
          리턴한다. 위치 아규먼트가 전달되지 않은 경우에는 1부터 30의 값을 가지고 type에
          따른 리스트를 생성하여 리턴한다.
          type 이 2이면
                 데이터 값들에서 짝수에 해당하는 데이터들만을 가지고 리스트 생성
          type 이 3이면
                 데이터 값들에서 홀수에 해당하는 데이터들만을 가지고 리스트 생성
	      type 이 4이면
                 데이터 값들에서 10보다 큰 데이터들만을 가지고 리스트 생성
          type 이 1이면
                 데이터 값들을 모두 가지고 리스트 생성

          리스트 생성은 리스트 컴프리핸션(지능형 리스트) 구문을 사용한다.

3. 다양한 구성으로 아규먼트를 전달하면서 createList() 함수를 호출하고 리턴 결과를
   화면에 출력한다.
"""
def createList(*p, type=1):
    if len(p) > 0:
        if type == 2:
            newList = [n for n in p if n % 2 == 0]
        elif type == 3:
            newList = [n for n in p if n % 2]
        elif type == 4:
            newList = [n for n in p if n > 10]
        elif type == 1:
            newList = [n for n in p]
        return newList
    elif len(p) == 0:
        p = [n for n in range(1, 31)]
        if type == 2:
            newList = [n for n in p if n % 2 == 0]
        elif type == 3:
            newList = [n for n in p if n % 2]
        elif type == 4:
            newList = [n for n in p if n > 10]
        elif type == 1:
            newList = [n for n in p]
        return newList

print(createList(1, 20, 3, 4, 50, 6, 70, 8, 90, 10, type=2))
print(createList(1, 20, 3, 4, 50, 6, 70, 8, 90, 10, type=3))
print(createList(1, 20, 3, 4, 50, 6, 70, 8, 90, 10, type=4))
print(createList(1, 20, 3, 4, 50, 6, 70, 8, 90, 10))
print("*" * 111)
print(createList())
print(createList(type=2))
print(createList(type=3))
print(createList(type=4))


