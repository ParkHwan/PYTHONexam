import random
number1 = random.randint(5, 10)
number2 = 1
mul = 0
print("선택된 숫자", number1)
while number1 >= number2:
    mul = number2 * number2
    print(number2, "->", mul)
    # print(number2, "->", number2 ** 2)
    number2 += 1

