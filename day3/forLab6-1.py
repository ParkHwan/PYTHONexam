multiNum = 0
print("1부터 100까지의 숫자들 중에서")
for x in range(1, 101):
    for y in range(1, 101):
        if x % y == 0:
            multiNum += y
    print(x, "배수의 합은", multiNum, "이다.")
