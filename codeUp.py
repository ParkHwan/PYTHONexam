num = int(input("숫자를 입력하세요 : "))
for x in range(1 ,num+1):
    if x % 10 == 3 or x % 10 == 6 or x % 10 == 9:
        if x // 10 == 3 or x // 10 == 6 or x // 10 == 9:
            print("짝짝", end=" ")
        else:
            print("X", end=" ")
    elif x // 10 == 3 or x // 10 == 6 or x // 10 == 9:
        print("X", end=" ")
    else:
        print(x, end=" ")