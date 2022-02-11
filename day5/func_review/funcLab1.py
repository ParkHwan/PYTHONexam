def print_book_title():
    print('파이썬정복')


def print_book_publisher():
    print('한빛미디어')

print_book_title()
print_book_title()
print_book_title()
print_book_publisher()
print_book_publisher()
print_book_publisher()
print_book_publisher()
print_book_publisher()

print("**추가**")
for _ in range(3):
    print_book_title()
for _ in range(5):
    print_book_publisher()