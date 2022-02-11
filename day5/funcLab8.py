def print_triangle_withdeco(num, deco = "%"):
    if 1 <= num <= 10:
        for x in range(1, num+1):
            print(" " * (num-x) + deco * x)
    else:
        num = 5
        for x in range(1, num+1):
            print(" " * (num-x) + deco * x)

print_triangle_withdeco(5, "$")
print("-" * 20)
print_triangle_withdeco(5)
print("-" * 20)
print_triangle_withdeco(15, "*")
print("-" * 20)