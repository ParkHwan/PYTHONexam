def calcsum(n):
    """1 ~ n까지의 합계를 구해 리턴한다.
      n : 1부터 n 값까지의 합산한 값을 리턴
      """
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

print(calcsum(10))
print("[ help() 함수를 통해서 함수에 대한 설명 보기 ]")
help(calcsum) # 유저가 필요에 의해 정의한 함수, 유저
print("-"*60)
help(print) # 빌트인 function, 파이썬에 내장된 함수

