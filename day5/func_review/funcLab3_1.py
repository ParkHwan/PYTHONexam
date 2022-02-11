def expr(i, j, k):
    m = None
    if j == '+':
        m = i + k
    elif j == '-':
        m = i - k
    elif j == '*':
        m = i * k
    elif j == '/':
        m = i / k
    return m


num1 = int(input('계산할 첫번째 숫자 : '))
operator = input('연산식 사칙연산만가능 : ')
num2 = int(input('계산할 두번째 숫자 : '))
result = expr(num1, operator, num2)
if result == None:
    print("수행 불가")
else:
    print('연산결과 :', result)