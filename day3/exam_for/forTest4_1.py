for x in range(1, 51):
    if x % 10 == 0:
        print('+', end= '')
    else:
        print('-', end = '')
print()
print()

for x in range(1, 6):
    print('-' * 9, end = '')
    print('+', end = '')
print('\n')  # / (슬래쉬: 구분하는 역할(폴더)), \ (빽슬래쉬), 이스케이프 문자(기능문자) -> \n (개행문자), \t(탭문자)

for x in range(1, 51):
    if x % 5 == 0:
        print('+', end= '')
    else:
        print('-', end = '')
print('\n\n')

for x in range(1, 51):
    if x % 10 == 5:
        print('+', end= '')
    else:
        print('-', end = '')

