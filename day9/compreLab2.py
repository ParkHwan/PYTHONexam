"""[ 실습 2 ]
1. 파일명 : compreLab2.py

2. 구현해야 하는 함수 사양
   함수명 : mycompredict
   매개변수 : 가변 키워드형(0 개 이상의 키=값 형식의 아규먼트를 받아서 처리한다.)
   리턴값 : 1개
   기능 : funcLab12.py 에서 구현한 mydict() 라는 함수의 기능과 동일하게 구현하는데
        이번에는 딕셔너리 컴프리핸션(지능형 딕셔너리) 구문을 사용해서 생성한다.

3. 다양한 구성으로 가변 키워드 아규먼트를 전달하면서 mycompredict() 함수를 호출하고 리턴
결과를 화면에 출력한다.
"""
def mycompredict(**kwargs):
    if len(kwargs) == 0:
        return {}
    else:
        ex_dic = {"my"+k: v for k, v in kwargs.items()}
        return ex_dic

print(mycompredict(name = "JJangGu", age = 7, address = "사이타마현"))
print(mycompredict(name = "hwan", age = 39, address = "서울시 송파구"))
print(mycompredict(education = "빅데이터분석", day = 9, goal = "열심히 하겠습니다."))
print(mycompredict())