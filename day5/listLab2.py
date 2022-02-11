listnum = [10, 5, 7, 21, 4, 8, 18]
min = listnum[0]
for x in range(1, len(listnum)):
    if min > listnum[x]:
        min = listnum[x]
print("최소값 :", min)