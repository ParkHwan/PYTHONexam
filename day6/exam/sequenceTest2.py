list1 = [10, 20, 30, "가나다", "abc", "A", True, 10, 20, 10]
print(list1)     # [10, 20, 30, "가나다", "abc", "A", True, 10, 20, 10]
print("---in과 not in 연산자---")
print('30' in list1) # False
print(30 not in list1) # Fals
print(True in list1) # True
print(False not in list1) # True
print("---시퀀스연산---")
list2 = ["파","이","썬"]
print(list1+list2) # [10, 20, 30, "가나다", "abc", "A", True, 10, 20, 10, "파", "이", "썬"]
print(list1) # [10, 20, 30, "가나다", "abc", "A", True, 10, 20, 10]
print(list2) # ["파","이","썬"]
print(list2 * 3) # ["파","이","썬", "파","이","썬", "파","이","썬"]
print("---인텍싱과 슬라이싱---")
print(list2[0]); print(list2[1]); print(list2[2]); print(list2[-1]) # 파 이 썬 썬
print(list1[:]) # [10, 20, 30, "가나다", "abc", "A", True, 10, 20, 10]
print(list1[::1]) # [10, 20, 30, "가나다", "abc", "A", True, 10, 20, 10]
print(list1[::2]) # [10, 30, "abc", True, 20]
print(list1[::-1]) # 역순
print(list1[0:4:1]) # # [10, 20, 30, "가나다"]
print("---함수들---")
print(len(list1)) # 10
#print(max(list1)); print(min(list1))
print(max([10,20, 30])); print(min([10, 20,30])) # 30, 10
print(max(['a', 'b', 'c'])); print(min(['a', 'b', 'c'])) # c, a
print(max([True, False])); print(min([True, False])) # True ,False
print(list1.count(10)) # 3
print(list1.count(20)) # 2
print("---for와 함께 사용하는 시퀀스---")
for data in list2 :
    print("#", data, "#") # # 파 #, # 이 #, # 썬 #
print("---리스트는 변경가능---")
list2[0] = "가"
print(list2) # ["가","이","썬"]
list2[0:1] = "파"
print(list2) # ["파","이","썬"]
list2[0:0] = "가"
print(list2) # ["가", "파","이","썬"]
list2[0:2] = "나"
print(list2) # ["나","이","썬"]
list2[0:2] = [10, 20, 30, 40, 50, 60, 70]
print(list2) # [10, 20, 30, 40, 50, 60, 70, "썬"]
list2[0] = [10, 20, 30, 40, 50, 60, 70]
print(list2) # 인덱싱 방식은 리스트가 그대로 삽입
list2[0:1] = [10, 20, 30, 40, 50, 60, 70] # 슬라이싱 방법이면 리스트에 원소값이 순차적으로 들어간다
print(list2) # [[10, 20, 30, 40, 50, 60, 70], 20, 30, 40, 50, 60, 70, "썬"]
del list2[0]
print(list2) # [20, 30, 40, 50, 60, 70, "썬"]
del list2[0:3]
print(list2) # [50, 60, 70, "썬"]
r1 = list2.remove("썬")
print(list2) # [50, 60, 70]
print(r1) # None
#list2.remove("썬")
#print(list2)
r2 = list2.pop()
print(list2) # [50, 60]
print(r2) # 70
list2.append("가")
print(list2) # [50, 60, "가"]
list2.insert(1,"나")
print(list2) # [50, "나", 60, "가"]
list2.append([1,2,3])
print(list2) # [50, "나", 60, "가", [1, 2, 3]]
list2.extend([1,2,3,4,5])
print(list2) # [50, "나", 60, "가", 1, 2, 3, 4, 5]