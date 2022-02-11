# [ 실습 1 ]
# 1. 파일명 : funcLab7.py
# 2. 구현해야 하는 함수 사양
#    함수명 : print_gugudan
#    매개변수 : 1개
#    리턴값 : 없음
#    기능 : 전달된 숫자의 구구단을 출력한다.
#          - 전달된 아규먼트가 int 타입인지 채크하고 int 타입이 아니면 그냥 리턴한다.
#          - 전달된 아규먼트가 1~9 사이인지 채크하고 아니면 그냥 리턴한다.
#          - 그 외의 경우에는 해당 단의 구구단을 행 단위로 출력한다.\\
# 3. 숫자를 다양하게 지정해서 print_ gugudan() 함수를 호출해 본다.

# CASE1
def print_gugudan(num):
    if type(num) != int:
        return
    else:
        if 1 <= num <= 9:
            print(f'***구구단 {num} 단 ***')
            for i in range(1, 10):
                print(f'{num} x {i} = {num * i }')

print_gugudan(5)
print_gugudan(10)
print_gugudan(4)
print_gugudan("가")

# CASE2
def print_gugudan(num):
    if type(num) == int:
        if 1 <= num <= 9:
            print(f'***구구단 {num} 단 ***')
            for i in range(1, 10):
                print(f'{num} x {i} = {num * i }')
print_gugudan(5)
print_gugudan(10)
print_gugudan(4)
print_gugudan("가")

# CASE3
def print_gugudan(num):
    if type(num) == int and  1 <= num <= 9:
        print(f'***구구단 {num} 단 ***')
        for i in range(1, 10):
            print(f'{num} x {i} = {num * i }')
print_gugudan(5)
print_gugudan(10)
print_gugudan(4)
print_gugudan("가")
