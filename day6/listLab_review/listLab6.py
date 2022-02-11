numlist=[
    [10,12,14,16],
    [18,20,22,24],
    [26,28,30,32],
    [34,36,38,40]
]

print('1행 1열의 데이터:',numlist[0][0])
print('3행 4열의 데이터:',numlist[2][3])
print('행의 개수:',len(numlist))
print('열의 개수:',len(numlist[0]))
print('3행의 데이터들:',numlist[2][0],numlist[2][1],numlist[2][2],numlist[2][3]) #numlist[2][:]
print('2열의 데이터들:',numlist[0][1],numlist[1][1],numlist[2][1],numlist[3][1]) #numlist[:][1]
print('왼쪽 대각선 데이터들:',numlist[0][0],numlist[1][1],numlist[2][2],numlist[3][3])
print('오른쪽 대각선 데이터들:',numlist[0][-1],numlist[1][-2],numlist[2][-3],numlist[3][-4])


