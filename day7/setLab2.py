"""[ 실습 4 ]
1. setLab2.py 이라는 소스를 생성한다.
2. 비어있는 셋을 하나 만들고 이 안에 1~45 사이의 난수를 추출하여 6개를 저장하는데
   당연히 여기서도 동일한 숫자가 중복하여 저장되지 않게 한다.
3. 수행 결과는 다음과 같다.

	행운의 로또번호  : X, X, X, X, X, X
"""
lottoList = set()
import random
while True:
    if len(lottoList) < 6:
        random_num = random.randint(1, 45)
        lottoList.add(random_num)
    else:
        break
print("행운의 로또번호 : ", end="")
i = 0
for x in lottoList:
    if i < len(lottoList)-1:
        print(x, ", ", sep="", end="")
        i += 1
    else:
        print(x)
