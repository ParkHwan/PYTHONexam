while True:
    y, m = input("해당하는 년도와 월을 /로 나눠서 입력하시오: ").split("/")
    try:
        year = int(y)
        month = int(m)
        print(f"{year}년도 {month:02d}월")
        break
    except ValueError:
        print("입력된 값이 숫자가 아닙니다. 숫자로 입력해 주세요!!")

