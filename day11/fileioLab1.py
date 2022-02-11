import os
import datetime
if not os.path.isdir("c:/iotest"):
    os.mkdir("c:/iotest")
f = open("c:/iotest/today.txt", "wt", encoding="UTF-8")
now = datetime.datetime.now()
days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
f.write(f"오늘은 {now.year}년 {now.month}월 {now.day}일 입니다."
        f"\n오늘은 {days[now.weekday()]}입니다."
        f"\n나는 {days[now.weekday()]}에 태어났습니다.")
f.close()
print("저장이 완료되었습니다.")
