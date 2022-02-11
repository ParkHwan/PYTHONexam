"""[ 실습 4 ]
1. listLab8.py 이라는 소스를 생성한다.
2. 다음과 같은 내용으로 구성되는 이차원 리스트를 생성한다.
     'B', 'C', 'A', 'A'
     'C', 'C', 'B', 'B'
     'D', 'A', 'A', 'D'
3. 다음 내용으로 구성되는 리스트를 하나 생성한다.
    첫 번째 원소에는 'A' 문자의 개수
    두 번째 원소에는 'B' 문자의 개수
    세 번째 원소에는 'C' 문자의 개수
    네 번째 원소에는 'D' 문자의 개수

4. 다음과 형식으로 출력한다.
    A 는 x개 입니다.
    B 는 x개 입니다.
    C 는 x개 입니다.
    D 는 x개 입니다.
"""
munjaList = [["B", "C", "A", "A"],
             ["C", "C", "B", "B"],
             ["D", "A", "A", "D"]]
elementList = []
for x in munjaList:
    elementList += x
a = elementList.count("A")
b = elementList.count("B")
c = elementList.count("C")
d = elementList.count("D")
del elementList[:]
elementList.extend([a, b, c, d])
print("munjaList 내의 A, B, C, D의 갯수로 구성된 리스트 :", elementList)
alphabet = 65
for i in range(len(elementList)):
    if i < len(elementList):
        print(chr(alphabet), "는 ", elementList[i], "개 입니다. ", sep="")
    else:
        print(elementList[i])
    alphabet += 1
