data = input("데이터를 입력하세용 : ")
print("[" + data + "]")
if len(data) == 0: #len 문자의 길이를 나타낸다, 한글이나 영문 등 언어 상관없이 문자 한글자를 1로 계산
    print("입력한 내용이 없네요")
else:
    print("입력한 내용 :", data)
    print("입력한 내용의 길이:", len(data))






