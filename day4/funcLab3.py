def expr(x, y, z):
    if z == "+":
        result = x + y
        return result
    elif z == "-":
        result = x - y
        return result
    elif z == "*":
        result = x * y
        return result
    elif z == "/":
        result = x / y
        return result
    else:
        return None

result = expr(10, 1, "+")
if result == None:
    print("수행불가")
else:
    print("연산결과 : ", result)
