num = int(input())
newNum = 1
origin = num
count = 0
while True:
    if origin != newNum:
        first = num // 10
        second = num % 10
        sum = first + second
        newNum = (second * 10) + (sum % 10)
        count += 1
        num = newNum
    else:
        print(count)
        break
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