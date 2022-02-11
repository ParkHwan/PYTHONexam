listnum = [10, 5, 7, 21, 4, 8, 18]
max = listnum[0]
min = listnum[0]
for x in range(1, len(listnum)):
    if max < listnum[x]:
        max = listnum[x]
    elif min > listnum[x]:
        min = listnum[x]
print("최소값 :", min, "최대값 :", max)