yoil = ["월", "화", "수", "목","금", "토", "일"]
food = ["갈비탕", "순대국", "칼국수", "삼겹살"]
menu = zip(yoil, food)
print(menu, type(menu))
for y, f in menu:
    print(f"{y}요일 메뉴 : {f}")
print("*"*20)
print("이거는 왜 비어있을까?") # zip은 1회성이라 한번 읽고나면 끝나기 때문에 다시 호출해서 실행해야 한다.
for data in menu:
    print(data)
print("*"*20)
for data in zip(yoil, food):
    print(data)
print("*"*20)
print("이거는 왜 비어있을까?")
for data in menu:
    print(data)
print("*"*20)
menu = zip(yoil, food)
d2 = dict(menu)
for y, f in d2.items():
    print("%s요일 메뉴 : %s" % (y, f))
print(d2)

print("*"*20)

zip1 = zip([1, 2, 3], [4, 5, 6])
zip2 = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
zip3 = zip("abc", "def")

print(type(zip1))
print(list(zip1))
print(list(zip2))
print(list(zip3))
print("이거는 왜 비어있을까?")
print(dict(zip1))
print(dict(zip3))
