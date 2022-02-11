"""[ 실습 2 ]
1. 파일명 : funcLab12.py
2. 구현해야 하는 함수 사양
   함수명 : mydict
   매개변수 : 가변 키워드형(키=값 형식으로 전달받을 수 있는 아규먼트 개수에 제한이 없다.)
   리턴값 : 1개
   기능 :  아규먼트는 키=값 형식으로 전달되며 몇 개가 전달되든 처리해야 한다.
             아규먼트가 한 개도 전달되지 않으면 비어있는 딕셔너리를 리턴한다.
 	 비어있는 딕셔너리를 생성한 다음 아규먼트로 전달된 키=값 쌍을 저장하는데
키는 앞에 my 를  붙여서 저장한다.
              생성된 딕셔너리를 리턴한다.

3. 다양한 구성으로 키워드 아규먼트를 전달하면서 mydic() 함수를 호출하고 리턴 결과를
   화면에 출력한다.
"""
def mydict(**data):
    ex_dic = {}
    if len(data) == 0:   # 구지 없어도 될 구문이다. 이미 ex_dic = {} 가 리턴 될 것이기 때문에
        return {}
    else:
        for key, value in data.items():
            new_key = "my" + key
            ex_dic[new_key] = value
        return ex_dic

print(mydict(name = "JJangGu", age = 7, address = "사이타마현"))
print(mydict())