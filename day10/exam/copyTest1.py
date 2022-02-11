# =============== varcopy  ===============
print(id(1))
print(id("가"))
a = 3
b = a
print("a = %d, b = %d" % (a, b))
print(id(a), id(b))

a = 5
print("a = %d, b = %d" % (a, b))
print(id(a), id(b))
print("리터럴 3의 id : ", id(3), "리터럴 5의 id : ", id(5))
# =============== listcopy  ===============
list1 = [ 1, 2, 3 ]
list2 = list1

list2[1] = 100
print(list1)
print(list2)
print(id(list1),id(list2))
# =============== listcopy2  ===============
list1 = [ 1, 2, 3 ]
list2 = list1.copy()

list2[1] = 100
print(list1)
print(list2)
print(id(list1),id(list2))

