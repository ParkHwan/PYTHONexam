# CASE1
def number_all_sum(*p) :
    sum = 0
    numflag = False
    if len(p) == 0:         # 전달된 아규먼트에 숫자가 없다라는 조건 구현 필요
        return None
    else:
        for num in p:
            if type(num) == int:
                sum += num
                numflag = True
        if not numflag:
            sum = None
        return sum

print(number_all_sum(1, 2, 3, 4, 5))
print(number_all_sum(1, 2, 'a', 3, 4, 'b', 5))
print(number_all_sum(10, 20, True))
print(number_all_sum())
print(number_all_sum('a', True, '가'))
print(number_all_sum(0, 0, 0))
print("-"*50)
# CASE2
def number_all_sum(*args):
    result=0
    for i in args:
        if type(i) == int:
            result+=i
        '''elif type(i) == str:
            continue
        elif type(i) == bool:
            continue'''
    if result == 0:
        return None
    else:
        return result


print(number_all_sum(1, 2, 3, 4, 5))
print(number_all_sum(1, 2, 'a', 3, 4, 'b', 5))
print(number_all_sum(10, 20, True))
print(number_all_sum())
print(number_all_sum('a', True, '가'))
print(number_all_sum(0, 0, 0))


        
