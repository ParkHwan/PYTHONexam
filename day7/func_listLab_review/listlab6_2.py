list1=[ [10,12,14,16]
        ,[18,20,22,24]
        ,[26,28,30,32]
        ,[34,36,38,40]
        ]
print("1행 1열의 데이터 :", list1[0][0])
print("3행 4열의 데이터 :", list1[2][3])
print("행의 갯수:", len(list1))
print("열의 갯수:", len(list1[0]))
print("3행의 데이터들 :",end="")
for a in list1[2]:
        print(a, end=" ")
print("\n2열의 데이터들 :",end="")
for i in range(len(list1)):
        print(list1[i][1],end=" ")

print("\n왼쪽 대각선 데이터들 :",end="")
for a in range(len(list1)):
        print(list1[a][a],end=" ")

print("\n오른쪽 대각선 데이터들 :",end="")
for i in range(len(list1)):
        print(list1[i][3-i],end=" ")