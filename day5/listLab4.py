listnum = []
import random
for _ in range(10):
    listnum.append(random.randint(1, 50))
print(listnum)
for y in range(len(listnum)):
    if listnum[y] < 10:
        listnum[y] = 100
print(listnum)
print(listnum[0])
print(listnum[-1])
print(listnum[1:7])
print(listnum[::-1])
print(listnum[:])
del listnum[4]
print(listnum[::])
del(listnum[2:4])
print(listnum[::1])