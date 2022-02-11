import random
start = random.randint(1, 10)
end = random.randint(30, 40)
start + end == sum
for sum in (start,end):
    if (sum%2 == 0):
        print(start,'부터',end,'까지의 짝수의 합 :',sum)

print()

start = random.randint(1, 10)
end = random.randint(30, 40)
sum = 0
for data in range(start,end+1):
    if data % 2 == 0:
        sum = sum + data  # sum += data
print(start,'부터',end,'까지의 짝수의 합 :',sum)
