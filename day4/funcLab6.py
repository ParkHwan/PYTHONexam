def differtwonalue(x, y):
    if x < y:
        result = y - x
    elif x > y:
        result = x - y
    elif x == y:
        result = 0
    return result

import random
for _ in range(5):
    a1 = random.randint(1, 30)
    a2 = random.randint(1, 30)
    same = differtwonalue(a1, a2)
    print(a1, "와", a2, "의 차는", same, "입니다.")

for _ in range(5):
    print(a1, "와", a2, "의 차는", same, "입니다.")
