"""1. setLab1.py 이라는 소스를 생성한다.
2. 비어있는 셋을 2개 만들고 각각 1~20 사이의 숫자 10개를 추출하여 저장한다.
3. 생성된 2 개의 셋에 대하여 집합 연산을 수행하고 결과를 다음과 같이 출력한다.

	집합 1 : {x, x, x, x, x, x, x, x, x, x }
       	집합 2 : {x, x, x, x, x, x, x, x, x, x }
       	두 집합에 모두 있는 데이터 : {x, x, x, x, x, x, x }
	집합1 또는 집합2 에 있는 데이터 : {x, x, x, x, x, x, x }
	집합1에는 있고 집합2에는 없는 데이터 : {x, x, x, x, x, x, x }
	집합2에는 있고 집합1에는 없는 데이터 : {x, x, x, x, x, x, x }
	집합1과 집합 2가 각자 가지고 있는 데이터 : {x, x, x, x, x, x, x }
"""
import random
a = set()
b = set()
while True:
    if len(a) < 10:
        x = random.randint(1, 20)
        a.add(x)
    elif len(b) < 10:
        y = random.randint(1, 20)
        b.add(y)
    else:
        break

print("집합 1 :", a)
print("집합 2 :", b)
print("두 집합에 모두 있는 데이터: ", a & b)
print("집합1 또는 집합2 에 있는 데이터 :", a.union(b))
print("집합1에는 있고 집합2에는 없는 데이터 :", a.difference(b))
print("집합2에는 있고 집합1에는 없는 데이터 :", b - a)
print("집합1과 집합2가 각자 가지고 있는 데이터 :", a ^ b)
