def print_triangle(i):
    if 0 < i < 11:
        k = i+1
        for j in range(1, i+1, 1):
            k -= 1
            print('@'*k)

star_num = int(input('@ 갯수 1~10개사이 : '))
print_triangle(star_num)
