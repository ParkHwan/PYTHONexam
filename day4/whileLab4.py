while True:
    number = int(input("1~12 사이의 숫자를 입력하세요 :")) # 변수명은 month
    if number == 1 or number == 2 or number == 12:
        print(number, "월은 겨울")
    elif number == 3 or number == 4 or number == 5: # elif 3 <= month <= 5:
        print(number, "월은 봄")
    elif number == 6 or number == 7 or number == 8: # elif 6 <= month <= 8:
        print(number, "월은 여름")
    elif number == 9 or number == 10 or number == 11: # elif 9 <= month <= 11:
        print(number, "월은 가을")
    else:
        print("1~12 사이의 값을 입력하세요!")
        break
