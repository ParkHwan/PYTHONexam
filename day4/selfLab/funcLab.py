"""def print_book_title():
    print("파이썬 정복")
def print_book_publisher():
    print("한빛미디어")

print_book_title()
print_book_title()
print_book_title()
print_book_publisher()
print_book_publisher()
print_book_publisher()
print_book_publisher()
print_book_publisher()

def get_book_title():
    return "파이썬 정복"
def get_book_publisher():
    return "한빛미디어"

name = get_book_title()
print(name)
print(name)
print(get_book_publisher())

def expr(num1, num2, oper):
    if "+" in oper:
        result = num1 + num2
    elif "-" in oper:
        result = num1 - num2
    elif "*" in oper:
        result = num1 * num2
    elif "/" in oper:
        result = num1 / num2
    else:
        return None
    return result

returnValue = expr(12, 3, "*")
if returnValue:
    print(f"연산결과 :{returnValue}")
else:
    print("수행 불가")

def print_triangle(n):
    if 0 < n < 11:
        for x in range(1, n+1):
            print("*" * x)
    else:
        return

print_triangle(7)

def print_triangle(n):
    if 0 < n < 11:
        for x in range(n, 0, -1):
            print("@" * x)

print_triangle(2)
"""
import random
def differtwovalue(num1, num2):
    if num1 > num2:
        div = num1 - num2
    elif num1 < num2:
        div = num2 - num1
    else:
        return 0
    return div
for _ in range(5):
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    result = differtwovalue(num1, num2)
    print(f"{num1} 와 {num2} 의 차는 {result} 입니다.")
