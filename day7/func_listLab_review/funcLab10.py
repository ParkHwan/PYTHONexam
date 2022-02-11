# CASE1

def sumeven(*p):
    sum = 0
    for num in p:
        if num % 2 == 0:
            sum += num
    if len(p) == 0:
        sum = -1
    return sum

print(sumeven(1, 2, 3, 4, 5))
print(sumeven(11, 22, 33, 44, 55))
print(sumeven(1, 3, 5))
print(sumeven())
print("-"*50)
# CASE2

def sumeven(*args):
    result=0
    if args:
        for i in args:
            if i % 2 ==0:
                result += i
        return result
    else:
        return -1
print(sumeven(1, 2, 3, 4, 5))
print(sumeven(11, 22, 33, 44, 55))
print(sumeven(1, 3, 5))
print(sumeven())
