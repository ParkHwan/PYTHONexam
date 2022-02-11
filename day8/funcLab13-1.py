"""[ 실습 3 ]
1. 파일명 : funcLab13.py
2. 구현해야 하는 함수 사양
   함수명 : myprint
   매개변수 : 가변 아규먼트1개, 가변 키워드 아규먼트 1개
   리턴값 : 없음
   기능 : 전달되는 아규먼트의 개수에는 제한이 없다.
         호출시 전달되는 아규먼트의 데이터 타입에도 제한이 없다.
         아규먼트가 전달되지 않으면 “Hello Python”을 출력한다.
         출력 형식은 다음에 제시된 실행 결과 예시를 보고 처리하는데 반복문을 사용하지 않고 print()
함수로 처리한다.

 	 myprint(10, 20, 30, deco="@", sep="-")  호출시
     		@10-20-30@ 출력
	myprint("python", "javascript", "R", deco="$")  호출시
     		$python,javascript,R$ 출력
	myprint("가", "나", "다")  호출시
     		**가,나,다** 출력
	myprint(100)  호출시
     		**100** 출력
	myprint(True, 111, False, "abc", deco="&", sep="")  호출시
     		&True111Falseabc& 출력

3. 위에 제시된 호출식들을 가지고 호출했을 때 제시된 결과가 출력되면 완성이다.
"""
def myprint(*x, **y):
    if len(x) > 0:
        if "deco" in y:
            deco_string = y["deco"]
        else:
            deco_string = "**"
        if "sep" in y:
            sep_string = y["sep"]
        else:
            sep_string = ","

        print(deco_string, end="")
        print(*x, sep=sep_string, end="")
        print(deco_string)
    else:
        print("Hello Python")


myprint(10, 20, 30, deco="@", sep="-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")
myprint()
myprint(deco="^")