"""[ 실습 5 ]
1. 파일명 : funcLab10.py
2. 구현해야 하는 함수 사양
   함수명 : sumeven
   매개변수 : 가변형(전달받을 수 있는 아규먼트 개수에 제한이 없다.)
   리턴값 : 1개
   기능 : 아규먼트가 몇 개가 전달되든 처리해야 한다.
         아규먼트는 1 이상의 숫자만 온다고 정한다.
         전달된 아규먼트들에서 짝수에 해당하는 숫자들만 합을 계산해서 리턴한다.
         전달된 아규먼트들 중에 짝수가 없으면 0을 리턴한다.
         아규먼트가 전달되지 않으면 -1을 리턴한다.

3. 숫자를 다양하게 지정해서 sumEven() 함수를 호출해 본다.

	print(sumeven(1, 2, 3, 4, 5))
	print(sumeven(11, 22, 33, 44, 55))
	print(sumeven(1, 3, 5))
	print(sumeven())

	6
	66
	0
	-1

"""
def sumeven(*p):
    sum = 0
    for num in p:
        if num % 2 == 0:
            sum += num
    if len(p) == 0:
        sum = -1
    return sum

print(sumeven(1, 2, 3, 4, 5))
print(sumeven(11, 22, 33, 44, 55))
print(sumeven(1, 3, 5))
print(sumeven())