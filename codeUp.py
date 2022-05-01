"""num = int(input("숫자를 입력하세요 : "))
for x in range(1 ,num+1):
    if x % 10 == 3 or x % 10 == 6 or x % 10 == 9:
        if x // 10 == 3 or x // 10 == 6 or x // 10 == 9:
            print("짝짝", end=" ")
        else:
            print("X", end=" ")
    elif x // 10 == 3 or x // 10 == 6 or x // 10 == 9:
        print("X", end=" ")
    else:
        print(x, end=" ")

import pandas as pd
from glob import glob

file_names = glob("*.csv") #폴더 내의 모든 csv파일 목록을 불러온다
total = pd.DataFrame() #빈 데이터프레임 하나를 생성한다

for file_name in file_names:
    temp = pd.read_csv(file_name, engine='python', encoding='utf-8') #csv파일을 하나씩 열어 임시 데이터프레임으로 생성한다
    total = pd.concat([total, temp]) #전체 데이터프레임에 추가하여 넣는다

total.to_csv("total.csv")"""
def solve(a):
    ans = 0
    for n in a:
        ans += n
    return ans
a = [1, 2, 3, 4]
print(solve(a))
# 백준 4637번 문제
result = []
for b in range(10001):
    if b < 100:
        result.append(b + (b // 10) + (b % 10))
    elif b < 1000:
        result.append((b + (b // 100) + ((b - (b // 100) * 100) // 10) + ((b - (b // 100) * 100) % 10)))
    elif b < 10001:
        result.append(b + (b // 1000) + ((b - (b // 1000) * 1000) // 100) + (((b - (b // 1000) * 1000) - ((b - (b // 1000) * 1000) // 100) * 100) // 10)
                        + ((b - (b // 1000) * 1000) - ((b - (b // 1000) * 1000) // 100) * 100)  % 10)
    if not b in result:
        print(b)
