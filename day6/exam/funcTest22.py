print("---가변형 인자 함수 정의---")
def print_type(*p) :
    print("전달된 아규먼트 갯수 : ", len(p), "개", sep="")
    for data in p :
        print(type(data))
        print(data)

print_type(1, 2,'a', 3, 4, True, 5)
print_type([100, 200, 300])
print_type(3.4, 3, False, '가나다', '@')
print_type()

