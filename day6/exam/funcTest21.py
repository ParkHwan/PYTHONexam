print("---가변형 인자 함수 정의---")
def sum_all(*p) :
    """ 아규먼트로 전달되는 모든 숫자들의 합을 리턴"""
    print("p의 타입 :", type(p))
    sum = 0
    for data in p :
        sum += data
    return sum

print(sum_all(1,2,3,4,5))
print(sum_all(100, 200, 300))
print(sum_all(10,20,30,40,50,60,70))
print(sum_all())
