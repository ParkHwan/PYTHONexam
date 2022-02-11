"""[ 실습 3 ]
1. listLab7.py 이라는 소스를 생성한다.
2. 다음과 같은 내용으로 구성되는 이차원 리스트를 생성한다.
    1행   10, 20, 30, 40, 50
    2행   5, 10, 15
    3행  11, 22, 33, 44
    4행  9, 8, 7, 6, 5, 4, 3, 2, 13

 3. 행단위 합을 구하여 다음과 같이 출력한다.
    1행의 합은 x 입니다.
    2행의 합은 x 입니다.
    3행의 합은 x 입니다.
    4행의 합은 x 입니다.

"""
twodimensionlist = [[10, 20, 30, 40, 50],
           [5, 10, 15],
           [11, 22, 33, 44],
           [9, 8, 7, 6, 5, 4, 3, 2, 13]]
count = 0
for rowlist in twodimensionlist:
    linesum = 0
    for d in rowlist:
        linesum += d
    count += 1
    print(count, "행의 합은", linesum, "입니다.")
