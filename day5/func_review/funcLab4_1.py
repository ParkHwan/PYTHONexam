def print_triangle(i):
    if 0 < i < 11:
        k = 0
        for j in range(1, i+1, 1):
            k += 1
            print('*'*k)

star_num = int(input('별의 갯수 1~10개사이 : '))
print_triangle(star_num)
