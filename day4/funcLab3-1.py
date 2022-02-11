def expr(x, y, z):
    if z == "+":
        result = x + y
    elif z == "-":
        result = x - y
    elif z == "*":
        result = x * y
    elif z == "/":
        result = x / y
    else:
        result = None
    return result

returnValue = expr(1, 1, "-") # 문자 데이터, 문자 리터럴
if not returnValue: # None, "", [], 0 일때는 대부분 False로 간주
    print("수행불가")
else:
    print("연산결과 : ", returnValue)

returnValue = expr(1, 1, "+")
if returnValue == None:
    print("수행불가")
else:
    print("연산결과 : ", returnValue)
