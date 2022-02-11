score = [ 88, 95, 70, 100, 99 ]
no = 1
for s in score:
    print(str(no) + "번 학생의 성적 :", s)
    no += 1
print("-"*50)
for no, s in enumerate(score, 1):
    print(str(no) + "번 학생의 성적 :", s)
print("-"*50)
for data in enumerate(score, 1):
    print(data)
print("-"*50)
names = "둘리,고길동,희동이,마이콜,또치,도우너"
namelist = names.split(",")
print("정렬 전 :", namelist)
namelist.sort() # 오름차순 순(숫자는 작은거 부터 큰거까지, 문자도 작은값 부터 큰값까지), 원래 리스트를 직접적으로 변경
print("정렬 후 :", namelist)
for num, name in enumerate(namelist) :
    print(f"이름순으로 {name}는 {num+1}번입니다.")
for data in enumerate(namelist) :
    print(f"enumerate를 적용한 결과 : {data}")
for num, name in enumerate(namelist, 100) :
    print(f"이름순으로 {name}는 {num}번입니다.")



