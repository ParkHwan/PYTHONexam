"""[ 실습 2 ]
1. listLab6.py 이라는 소스를 생성한다.
2. 다음과 같은 내용으로 구성되는 이차원 리스트를 생성한다.

	10, 12, 14, 16
    	18, 20, 22, 24
    	26, 28, 30, 32
    	34, 36, 38, 40

3. 다음 결과를 출력한다.

	1행 1열의 데이터 : 10
   	3행 4열의 데이터 : 32
	행의 갯수 : 4
	열의 갯수 : 4
	3행의 데이터들 : 26 28 30 32
	2열의 데이터들 : 12 20 28 36
       왼쪽 대각선 데이터들 : 10 20 30 40
       오른쪽 대각선 데이터들 : 16 22 28 34

"""
listnum = [[10, 12, 14, 16],
            [18, 20, 22, 24],
            [26, 28, 30, 32],
            [34, 36, 38, 40]]

print("1행 1열의 데이터 :", listnum[0][0])
print("3행 4열의 데이터 :", listnum[2][3])
print("행의 갯수 :", len(listnum))
print("열의 갯수 :", len(listnum[0]))
# 제어문으로 행들의 데이터 및 대각선 데이터 구현
print("3행의 데이터들 :", listnum[2])
print("3행의 데이터를 : ", end="")
for a in listnum[2]:
    print(a, end=" ")
print("\n2열의 데이터들 :", listnum[0][1], listnum[1][1], listnum[2][1], listnum[3][1])
print("2열의 데이터들 : ", end="")
for i in range(len(listnum)):
    print(listnum[i][1], end=" ")
print("\n왼쪽 대각선들 :", listnum[0][0], listnum[1][1], listnum[2][2], listnum[3][3])
print("왼쪽 대각선들 : ", end="")
for a in range(len(listnum)):
    print(listnum[a][a], end=" ")
print("\n오른쪽 대각선들 :", listnum[0][3], listnum[1][2], listnum[2][1], listnum[3][0])
print("오른쪽 대각선들 : ", end="")
for i in range(len(listnum)):
    print(listnum[i][3-i], end=" ")