str = "89점"
try:
    score = int(str)
    print(score)
    a = str[5]
except ValueError as e:
    print("ㅠㅠ1 : ",e)
except IndexError as e:
    print("ㅠㅠ2 : ",e)
print("작업완료")


