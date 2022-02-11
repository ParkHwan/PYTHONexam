# CASE1
double=[['B','C','A','A'],['C', 'C', 'B', 'B'],['D', 'A', 'A', 'D']]
a=0
b=0 
c=0 
d=0
for i in double:
    for j in i:
        if j == "A":
            a+=1
        elif j == "B":
            b+=1
        elif j == "C":
            c+=1
        else:
            d+=1
list=[a,b,c,d]
print(list)
print("A는",a,"개 입니다.")
print("B는",b,"개 입니다.")
print("C는",c,"개 입니다.")
print("D는",d,"개 입니다.")
print("-"*50)
# CASE2
munjaList = [["B", "C", "A", "A"],
             ["C", "C", "B", "B"],
             ["D", "A", "A", "D"]]
elementList = []
for x in munjaList:
    elementList += x # ["B", "C", "A", "A", "C", "C", "B", "B", "D", "A", "A", "D"]
a = elementList.count("A")
b = elementList.count("B")
c = elementList.count("C")
d = elementList.count("D")
del elementList[:]
elementList.extend([a, b, c, d])
print("munjaList 내의 A, B, C, D의 갯수로 구성된 리스트 :", elementList)
alphabet = 65
for i in range(len(elementList)):
    if i < len(elementList):
        print(chr(alphabet), "는 ", elementList[i], "개 입니다. ", sep="")
    else:
        print(elementList[i])
    alphabet += 1
print("-"*50)

# CASE3

# 1. listLab8.py 이라는 소스를 생성한다.
# 2. 다음과 같은 내용으로 구성되는 이차원 리스트를 생성한다.
#      'B', 'C', 'A', 'A'
#      'C', 'C', 'B', 'B'
#      'D', 'A', 'A', 'D'
alphabat = [['B', 'C', 'A', 'A'],
            ['C', 'C', 'B', 'B'],
            ['D', 'A', 'A', 'D']]

# 3. 다음 내용으로 구성되는 리스트를 하나 생성한다.
#     첫 번째 원소에는 'A' 문자의 개수
#     두 번째 원소에는 'B' 문자의 개수
#     세 번째 원소에는 'C' 문자의 개수
#     네 번째 원소에는 'D' 문자의 개수
numOfalphpbat = [0,0,0,0]
for num in range(3):
    for alpha in alphabat[num]:
        if alpha == 'A':
            numOfalphpbat[0] += 1
        elif alpha == 'B':
            numOfalphpbat[1] += 1
        elif alpha == 'C':
            numOfalphpbat[2] += 1
        elif alpha == 'D':
            numOfalphpbat[3] += 1

# 4. 다음과 형식으로 출력한다.
#     A 는 x개 입니다.
#     B 는 x개 입니다.
#     C 는 x개 입니다.
#     D 는 x개 입니다.
print(f'A는 {numOfalphpbat[0]}개 입니다.')
print(f'B는 {numOfalphpbat[1]}개 입니다.')
print(f'C는 {numOfalphpbat[2]}개 입니다.')
print(f'D는 {numOfalphpbat[3]}개 입니다.')
print("-"*50)
# CASE4
ch_list = [['B', 'C', 'A', 'A'],
           ['C', 'C', 'B', 'B'],
           ['D', 'A', 'A', 'D']]

count_ch = [0, 0, 0, 0]

for row in ch_list:
    count_ch[0] += row.count('A')
    count_ch[1] += row.count('B')
    count_ch[2] += row.count('C')
    count_ch[3] += row.count('D')

print("A는 ", count_ch[0], "개 입니다.", sep='')
print("B는 ", count_ch[1], "개 입니다.", sep='')
print("C는 ", count_ch[2], "개 입니다.", sep='')
print("D는 ", count_ch[3], "개 입니다.", sep='')
