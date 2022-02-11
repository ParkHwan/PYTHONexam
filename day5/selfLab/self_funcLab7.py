""" 1. 파일명 : funcLab7.py
2. 구현해야 하는 함수 사양
   함수명 : print_gugudan
   매개변수 : 1개
   리턴값 : 없음
   기능 : 전달된 숫자의 구구단을 출력한다.
         - 전달된 아규먼트가 int 타입인지 채크하고 int 타입이 아니면 그냥 리턴한다.
         - 전달된 아규먼트가 1~9 사이인지 채크하고 아니면 그냥 리턴한다.
         - 그 외의 경우에는 해당 단의 구구단을 행 단위로 출력한다.\\
3. 숫자를 다양하게 지정해서 print_ gugudan() 함수를 호출해 본다."""

def print_gugudan(dan):
    if type(dan) == int and 0 < dan < 10:
        for x in range(1, 10):
            print(dan, "*", x, "=", dan * x, end="\t")
    else:
        return
print_gugudan(5)