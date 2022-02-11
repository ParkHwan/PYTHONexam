listnum = [10, 5, 7, 21, 4, 8, 18]
max = listnum[0]
for x in range(1, len(listnum)):
    if max < listnum[x]:
        max = listnum[x]
print("최대값 :", max)