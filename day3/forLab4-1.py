for x in range(9, 1, -1):
    if x % 2 == 0:
        print(x, ": 짝수", sep="")
    elif x < 4:
        break
    else:
        print(x, ": 홀수", sep="")

