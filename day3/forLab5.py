import random
start = random.randint(1, 10)
end = random.randint(30, 40)
evenNum = 0
for x in range(start, end + 1):
    if x % 2 == 0:
        evenNum += x
print(start, "부터", end, "까지의 짝수의 합:", evenNum)
