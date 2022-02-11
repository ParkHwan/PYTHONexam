""" [ 실습 4 ]
최댓값을 구하는 기능은 내장 함수(max())를 사용하지 않고 제어문으로 직접 구현한다.
1. listLab1.py 이라는 소스를 생성한다.
2. 다음 값들로 구성되는 리스트를 생성하여 listnum 에 저장한다.
   10, 5, 7, 21, 4, 8, 18
3. listnum 에 저장된 값들 중에서 최댓값을 추출하여 다음과 같이 출력한다.
"""
import random
listnum = []
for _ in range(10):
    listnum.append(random.randint(1, 100))
print(listnum)
maxValue = listnum[0]
minValue = listnum[0]
for x in range(1, len(listnum)):
    if maxValue < listnum[x]:
        maxValue = listnum[x]
    if minValue > listnum[x]:
        minValue = listnum[x]

print("최대값: ", maxValue, "최소값: ", minValue)