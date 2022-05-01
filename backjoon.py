# import sys
# num = int(sys.stdin.readline())
# newNum = 1
# origin = num
# count = 0
# while True:
#     first = num // 10
#     second = num % 10
#     sum = first + second
#     newNum = (second * 10) + (sum % 10)
#     count += 1
#     num = newNum
#     if origin == newNum:
#         print(count)
#         break
""" # 성민아
import sys
n = int(sys.stdin.readline())
origin = n
i = 0

while True:
    fst = n % 10
    snd = n // 10
    aa = snd + fst
    bb = (fst * 10) + (aa % 10)
    i += 1
    n = bb
    if bb == origin:
        break
print(i)
"""
"""
A = int(input()) # 박재현
count = 0
T = A / 10
O = A % 10
sum = int((T + O) % 10)
N = O * 10 + sum
count += 1
while True:
    if A == N:
        print(count)
        break
    elif A != N:
        T = A / 10
        O = A % 10
        sum = int((T + O) % 10)
        N = O * 10 + sum
        count += 1
"""
# 백준 if문 2525번 문제
# hour, min = map(int, (input().split()))
# cooktime = int(input())
# finish = min + cooktime
# while True:
#     if finish >= 60:
#         hour += 1
#         min = finish - 60
#         finish -= 60
#         if hour == 24:
#             hour = 0
#     else:
#         print(hour, finish)
#         break
# 백준 if 문 2480 문제
# num1, num2, num3 = map(int, (input().split()))
# if num1 == num2 == num3:
#     reward = 10000 + num1 * 1000
# elif num1 == num2 or num2 == num3:
#     reward = 1000 + num2 * 100
# elif num3 == num1:
#     reward = 1000 + num3 * 100
# else:
#     reward = max(num1, num2, num3) * 100
# print(reward)
# 백준 while문 10952번 문제
# sum = []
# while True:
#     a, b = map(int, input().split())
#     if a or b:
#         sum.append(a + b)
#     elif a == 0 and b == 0:
#         for x in sum:
#             print(x)
#         break
# 백준 1차원 배열 10818번 문제
n = int(input())

