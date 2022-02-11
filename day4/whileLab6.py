while True:
    mul = 1
    number = int(input("숫자를 입력하시오 :"))
    if number < -10 or number > 10:
        continue
    elif number > 0:
        print("입력값 :", number)
        for x in range(1, number+1):
            mul *= x
        print(mul)
    elif number < 0:
        number *= -1
        print("입력값(부호변경) :", number)
        for x in range(1, number+1):
            mul *= x
        print(mul)
    else:
        print("종료")
        break
