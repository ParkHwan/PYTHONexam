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
str = '무궁화 꽃이 피었습니다.'
new_str = str.replace('무궁화', '진달래')
'자바 언어를 알기 쉽게 설명하였다'.replace('자바', '파이썬')
idx = str.index('꽃')

print(new_str, idx)
# 이 시점에서 str의 값은 무엇일까요?
print(str)
print('자바 언어를 알기 쉽게 설명하였다'.replace('자바', '파이썬'))