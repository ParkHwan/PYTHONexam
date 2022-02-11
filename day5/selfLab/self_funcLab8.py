""" 1. 파일명 : funcLab8.py
2. 구현해야 하는 함수 사양
   함수명 : print_triangle_withdeco
   매개변수 : 2개
            숫자와 데코문자
            여기에서 데코문자는 기본값을 갖는다. 기본값은 ‘%’로 정한다.
   리턴값 : 없음
   기능 : 전달된 숫자 개수로 구성되는 삼각형을 출력한다. 출력 형식은 다음과 같다.
         숫자 2 만 전달시
           %
         %%
         숫자 5 와 데코문자 ‘*’ 전달시
             *
            **
           ***
          ****
         *****
1~10 이외의 값이 전달된 경우에는 5로 설정하여 출력한다.

3. 숫자를 다양하게 지정해서 print_triangle_withdeco () 함수를 호출해 본다.
"""
def print_triangle_withdeco(num, deco):
    if deco == True and 0 < num < 11:
        for x in range(1, num+1):
            print(" " * (num-x) + deco * x)
    elif deco == "":
        deco = "%"
        for x in range(1, num+1):
            print(" " * (num-x) + deco * x)
    else:
        num = 5
        for x in range(1, num+1):
            print(" " * (num-x) + deco * x)

num = int(input("1~10 사이의 숫자를 입력하시오: "))
deco = input("삼각형 표시할 문자를 입력하시오: ")
print_triangle_withdeco(num, deco)