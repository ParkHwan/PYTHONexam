import random # random 이라는 모듈을 가져다 쓰겠다!!
num = random.randint(1, 20) # 난수를 추출
if num % 2 == 0 :
    print(num, "은 짝수", sep="")
else :
    print(num, "은 홀수", sep="")
print("-"*50)

if num % 2 == 0 :
    print(num)
    print("은 짝수")
else :
    print(num)
    print("은 홀수")
print("-"*50)

if num % 2 == 0 :
    print(num, end="")
    print("은 짝수")
else :
    print(num, end="")
    print("은 홀수")
print("-"*50)