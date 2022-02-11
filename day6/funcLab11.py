"""[ 실습 6 ]
1. 파일명 : funcLab11.py
2. 구현해야 하는 함수 사양
   함수명 : number_all_sum
   매개변수 : 가변형(전달받을 수 있는 아규먼트 개수에 제한이 없다.)
   리턴값 : 1개
   기능 : 아규먼트가 몇 개가 전달되든 처리해야 한다.
         호출시 전달되는 아규먼트의 데이터 타입에는 제한이 없다. 그러므로 전달된 아규먼트의
         타입을 채크하여 숫자만 처리하고 숫자가 아닌 데이터는 무시한다.
         아규먼트가 전달되지 않았거나 전달되었다 하더라도 숫자가 없으면 None 을
	 리턴한다.

3. 숫자를 다양하게 지정해서 number_all_sum () 함수를 호출해 본다.
	print(number_all_sum(1, 2, 3, 4, 5))
	print(number_all_sum(1, 2, 'a', 3, 4, 'b', 5))
	print(number_all_sum(10, 20, True))
	print(number_all_sum())
    	print(number_all_sum('a', True, '가'))

       	15
       	15
       	30
	None
	None
"""
def number_all_sum(*p) :
    sum = 0
    numflag = False
    if len(p) == 0:         # 전달된 아규먼트에 숫자가 없다라는 조건 구현 필요
        return None
    else:
        for num in p:
            if type(num) == int:
                sum += num
                numflag = True
        if not numflag:
            sum = None
        return sum

print(number_all_sum(1, 2, 3, 4, 5))
print(number_all_sum(1, 2, 'a', 3, 4, 'b', 5))
print(number_all_sum(10, 20, True))
print(number_all_sum())
print(number_all_sum('a', True, '가'))
print(number_all_sum(0, 0, 0)) # Test
