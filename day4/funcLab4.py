def print_trangle(a):
    if a > 10:
        return
    else:
        for x in range(1, a+1):
            for y in range(x):
                print('*', end='')
            print()

print_trangle(5)
print("-" * 20)
print_trangle(7)
print("-" * 20)
print_trangle(9)