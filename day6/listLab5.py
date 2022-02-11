"""[ 실습 1 ]
1. listLab5.py 이라는 소스를 생성한다.
2. 비어있는 리스트를 하나 만들고 이 안에 1~45 사이의 난수를 추출하여 6개를 저장하는데
   동일한 숫자가 중복하여 저장되지 않게 한다.
3. 수행 결과는 다음과 같다.

	행운의 로또번호  : X, X, X, X, X, X
"""
lottoList = []
import random
for _ in range(6):
    random_num = random.randint(1, 45)
    while random_num in lottoList:
        random_num = random.randint(1, 45)
    lottoList.append(random_num)
print("행운의 로또번호 : ", end="")

for i in range(len(lottoList)):
    if i < len(lottoList)-1:
        print(lottoList[i], ", ", sep="", end="")
    else:
        print(lottoList[i])
