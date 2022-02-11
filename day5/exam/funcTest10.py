def add(num1, num2) : # 명시적으로 리턴값이 없음 -> 암시적인 리턴값은 있음 (None), 대부분 인터프립트 언어들 해당
    print(num1 + num2)

# 아규먼트: 함수를 호출할 때 소괄호에 담아서 전달하는 데이터
r1 = add(10, 20) # 리터럴
v1 = 100; v2 = 200
r2 = add(v1, v2) # 이미 값을 가지고 있는 변수(이미 정의(선언)된 변수)
print(r1)
print(r2)
print(add(1000, 2000)) # 함수 호출 식
#print(1+add(1000, 2000))  # 1 + None, None은 문자값으로 인식하고 있어서 에러 발생, 숫자 + 문자를 더하라는 명령이라서
print(bool(add(1000, 2000)))  # False
print(1+bool(add(1000, 2000))) # 1, bool(None) -> Fasle, int(False) -> 0
# print(1 + "bool") # 에러