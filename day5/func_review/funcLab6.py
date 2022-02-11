def differtwovalue(num1,num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1

import random
for _ in range(5):
    num1 = random.randint(1, 30)
    num2 = random.randint(1, 30)
    print(num1,'와',num2,'의 차는',differtwovalue(num1,num2),'입니다.')
'''
print("="*20)
for _ in range(5):
    print(random.randint(1, 30),'와',random.randint(1, 30),'의 차는',differtwovalue(random.randint(1, 30),random.randint(1, 30)),'입니다.')
'''
