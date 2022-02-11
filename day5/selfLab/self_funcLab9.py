""" [ 실습 3 ]
1. 파일명 : funcLab9.py
2. 구현해야 하는 함수 사양
   함수명 : isPYTHON
   매개변수 : 1개
            문자열
   리턴값 : bool 타입의 값
   기능 : 전달된 문자열에 PYTHON 이 존재하는지 채크하고 존재하면 True를 존재하지 않으면
False를 리턴한다.

3. 다음과 같이 isPYTHON() 을 호출하고 리턴 결과가 참이면 “PYTHON이 존재합니다”
거짓이면 “PYTHON이 존재하지 않습니다”를 화면에 출력한다.

		isPYTHON("나는 PYTHON을 학습합니다. ")
       		isPYTHON("나는 python을 학습합니다. ")
		isPYTHON("PYTHON1234")

"""
def isPYTHON(munja):
    if "PYTHON" in munja:
        print("PYTHON이 존재합니다.")
        return True
    else:
        print("PYTHON이 존재하지 않습니다.")
        return False

isPYTHON("나는 PYTHON을 학습합니다. ")
isPYTHON("나는 python을 학습합니다. ")
isPYTHON("PYTHON1234")
