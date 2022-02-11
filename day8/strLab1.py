"""
[ 실습 4 ]
1. 파일명 : strLab1.py
2. 구현해야 하는 함수 사양
   함수명 : myemail_info
   매개변수 : 이메일 주소 문자열 1개
   리턴값 : 2개의 원소를 갖는 튜플
   기능 : 전달된 이메일 주소 문자열에서 @ 를 기준으로 쪼개서 튜플을 만들어 리턴한다.
         단, 전달된 문자열에 @가 없으면 None을 리턴한다.

3. 아규먼트를 전달하면서 myemail_info() 함수를 여러 번 호출하고 리턴 결과를
   화면에 출력한다.
"""
def myemail_info(e):
    if "@" in e:
        x = e.split("@")
        y = tuple(x)
        return y   # return tuple(e.splt("@") 2줄을 줄여서 리턴으로 바로 가능!!
    else:
        return None

print(myemail_info("1235@naver.com"))
print(myemail_info("asdlkjfei@naver@gmail.com"))
print(myemail_info("naver.com"))
