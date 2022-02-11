import random
list=[]
i=0
while i<6:
    num=random.randrange(1,46)
    if num not in list:
        list.append(num)
        i+=1
print("행운의 로또번호 : ", list[0],",",list[1],",",list[2],",",list[3],",",list[4],",",list[5])

for i in range(len(list)):
    if i < len(list)-1 :
        print(list[i], ", ", sep="", end="")
    else:
        print(list[i])


