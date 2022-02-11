# =============== index  ===============
s = "python"
print(s[2])           #t 출력
print(s[-2])          #o 출력

# =============== stringindex  ===============
s = "python"
for c in s:
    print(c, end="")            #python 출력

# =============== slice  ===============
s = "python"
print("\n"+s[2:5])         #개행처리 후 tho 출력
print(s[3:])               #hon 춫력
print(s[:4])               #pyth 출력
print(s[2:-2])             #th 출력
print(s[2:4])              #th 출력

# =============== slice2  ===============
file = "20171224-104830.jpg"
print("촬영 날짜 : " + file[4:6] + "월 " + file[6:8] + "일")               # 촬영 날짜 : 12 월 24일
print("촬영 시간 : " + file[9:11] + "시 " + file[11:13] + "분")            # 촬영 시간 : 10 시 48분
print("확장자 : " + file[-3:])                                             # 확장자 : jpg

print(file.index("."))                                                     # 15
print("확장자 : " + file[file.index(".")+1:])                              # 확장자 : jpg

# =============== slice3  ===============
yoil = "월화수목금토일"
print(yoil[::2])           # 월수금일
print(yoil[::-1])          # 일토금목수화월

# =============== unpacking  ===============
a,b,c,d,e,f,g = yoil
print(a,b,c,d,e,f,g)            # 월 화 수 목 금 토 일

help(s.find)
help(s.index)

