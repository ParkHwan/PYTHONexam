"""num = int(input())
if num > 10:
    print("OK")

color_name = input()
if color_name == "red":
    print("##ff0000")
else:
    print("#000000")

import random
grade = random.randint(1, 6)
if grade >= 1 and grade <= 3:
    print(f"{grade}학년은 저학년입니다.")
if grade > 3 and grade <= 6:
    print(f"{grade}학년은 고학년입니다.")

import random
grade = random.randint(1, 6)
if grade == 1 or grade == 2 or grade == 3:
    print(f"{grade}학년은 저학년입니다.")
if grade == 4 or grade == 5 or grade == 6:
    print(f"{grade}학년은 고학년입니다.")

import random
score = random.randint(1, 100)
if 90 <= score <= 100:
    print(f"{score}점은 A등급입니다.")
elif 80 <= score < 90:
    print(f"{score}점은 B등급입니다.")
elif 70 <= score < 80:
    print(f"{score}점은 C등급입니다.")
elif 60 <= score < 70:
    print(f"{score}점은 D등급입니다.")
else:
    print(f"{score}점은 F등급입니다.")

num = int(input("1부터 10사이의 숫자를 하나 입력하세요 :"))
if 0 < num < 11:
    if num % 2:
        print(f"{num} : 홀수")
    else:
        print(f"{num} : 짝수")
else:
    print("1부터 10 사이의 값이 아닙니다.")
"""
import random
oper_num = random.randint(1, 10)
print(oper_num)
if oper_num == 1 or oper_num == 6:
    result = 300 + 50
elif oper_num == 2 or oper_num == 7:
    result = 300 - 50
elif oper_num == 3 or oper_num == 8:
    result = 300 * 50
elif oper_num == 4 or oper_num == 9:
    result = 300 / 50
else:
    result = 300 % 50
print(f"결과값 : {result}")