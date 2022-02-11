def print_gugudan(dan):
    if type(dan) == int and 1 <= dan <= 9:
        for num in range(1, 10):
            print(dan, "*", num, "=", dan * num, end="\t")
    else:
        return

print_gugudan(2)
print()
print_gugudan(3)
print()
print_gugudan(4)
print()
print_gugudan("rk")