def print_trangle(a):
    if a > 10:
        None
    else:
        for x in range(a, 0, -1):
            for y in range(x):
                print('@', end='')
            print()

print_trangle(5)
print("-" * 20)
print_trangle(7)
print("-" * 20)
print_trangle(9)