from MyError import NoNegativeNumberError

def set_age(age):
    if age < 0:
        raise NoNegativeNumberError("노노")
    else:
        print(f"당신의 나이는 {age}이군요!!")

try:
    set_age(int(input("나이를 입력하세요 : ")))
except NoNegativeNumberError as e:
    print(e)
except :
    print("숫자만!!")
finally:
    print("종료합니다.")