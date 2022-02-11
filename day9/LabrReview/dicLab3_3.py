team = {
         "박연서":{
                   "나이": 30,
                   "거주지역": "서울",
                   "메일주소": "yyeonseo.park@gmail.com",
                   "취미": ["전시회 감상", "사진촬영"],
                   "좋아하는 음식": ["고기", "와인"]
                  },
         "이영준":{
                   "나이": 26,
                   "거주지역": "부산",
                   "메일주소": "yeonseo.park@gmail.com",
                   "취미": ["컨텐츠 분석", "노래"],
                   "좋아하는 음식": ["감자탕", "스테이크"]
                  }
         }

for member in team:
    print(f"{member:<4} {team[member]['나이']:<4} {team[member]['거주지역']:4} {team[member]['메일주소']:25} {team[member]['취미']}   \t{team[member]['좋아하는 음식']}")
