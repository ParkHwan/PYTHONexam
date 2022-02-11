"""for n in range(1, 11):
    print(n, end=" ")
print()
for n in range(5):
    print(n)
for _ in range(5):
    print("@")
for x in range(9, 3, -1):
    if x % 2:
        print(f"{x} : 홀수")
    else:
        print(f"{x} : 짝수")

import random
start = random.randint(1, 10)
end = random.randint(30, 40)
print(start, end)
sum = 0
for n in range(start, end+1):
    if n % 2 == 0:
        sum += n
print(f"{start} 부터 {end} 까지의 짝수의 합 : {sum}")
"""
evenNum = 0
oddNum = 0
for x in range(1, 101):
    if x % 2 == 0:
        evenNum += x
    else:
        oddNum += x
print(f"1부터 100까지의 숫자들 중에서 \n짝수의 합은 {evenNum} 이고 \n홀수의 합은 {oddNum} 이다.")