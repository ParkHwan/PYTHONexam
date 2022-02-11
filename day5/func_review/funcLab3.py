def expr(num1,num2,deco):
    if deco == '+':
        result = num1 + num2
    elif deco == '-':
        result = num1 - num2
    elif deco == '*':
        result = num1 * num2
    elif deco == '/':
        result = num1 / num2
    else:
        result = None
    return result


returnValue = expr(1,2, '+') # 문자데이터, 문자리터럴
if returnValue == None:
    print("수행 불가")
else:
    print("연산 결과:", returnValue)

returnValue = expr(1,1,'-')
if returnValue == None:  # None, 0, "", [] == False
    print("수행 불가")
else:
    print("연산 결과:", returnValue)






