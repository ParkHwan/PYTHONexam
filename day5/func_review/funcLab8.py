# [ 실습 2 ]
# 1. 파일명 : funcLab8.py
# 2. 구현해야 하는 함수 사양
#    함수명 : print_triangle_withdeco
#    매개변수 : 2개
#             숫자와 데코문자
#             여기에서 데코문자는 기본값을 갖는다. 기본값은 ‘%’로 정한다.
#    리턴값 : 없음
#    기능 : 전달된 숫자 개수로 구성되는 삼각형을 출력한다. 출력 형식은 다음과 같다.
#          숫자 2 만 전달시
#          %
#          %%
#          숫자 5 와 데코문자 ‘*’ 전달시
#              *
#             **
#            ***
#           ****
#          *****
# 1~10 이외의 값이 전달된 경우에는 5로 설정하여 출력한다.
# CASE1
def print_triangle_withdeco(num,deco):
    if deco == '':  # 널문자열
        deco = '%'

    for i in range(1, num+1):
        print(' '*(num-i), deco * i, sep="")

num = int(input('정수 숫자를 입력하세요>>'))
deco = input('데코 문자를 입력하세요(기본값은 %)>>')

print_triangle_withdeco(num, deco)

# CASE2
def print_triangle_withdeco(num,deco='%'):
    for i in range(1, num+1):
        print(' '*(num-i), deco * i, sep="")

num = int(input('정수 숫자를 입력하세요>>'))
deco = input('데코 문자를 입력하세요(기본값은 %)>>')

if deco:
    print_triangle_withdeco(num, deco)
else:
    print_triangle_withdeco(num)
