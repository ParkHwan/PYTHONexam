def myfunc(p1, p2, p3):
    print("***myfunc() 에서의 출력***")
    print(p1)
    print(p2)
    print(p3)
    print("*"*27)


listv = [1,2,3]
listv1 = [1,2,3]
tuplev = 10,20,30

v1, v2, v3 = listv
print(v1)
print(v2)
print(v3)

v4, v5, v6 = tuplev
print(v4)
print(v5)
print(v6)
print("-"*27)
myfunc(*listv1) # 아규먼트에 별을 붙이면 언패킹해서 전달
myfunc(*tuplev)