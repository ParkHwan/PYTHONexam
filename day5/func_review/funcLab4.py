def print_triangle(num):
    if 1<= num <= 10:
        for i in range(1,num+1):
            print('*'*i)


print_triangle(3)
print("-"*20)
print_triangle(5)
print("-"*20)
print_triangle(11)
print("-"*20)
print_triangle(1)