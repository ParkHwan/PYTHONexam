dics = { '강승준': { '나이':28, '거주지역': '서울', '메일주소': 'rkdtmdwns0105@gmail.com',
                 '취미': ('게임,운동'), '좋아하는 음식': ('치킨,떡볶이,추어탕') },
        '권진우': { '나이':32, '거주지역': '서울', '메일주소': 'dncednce@daum.net',
                 '취미': '유튜브', '좋아하는 음식': ('회, 초밥, 중국음식') },
        '성민아': { '나이':27, '거주지역': '성남', '메일주소': 'sma0608@naver.com',
                 '취미': ('유튜브,게임'), '좋아하는 음식': ('초밥, 국밥, 치킨') },
        '조민석': { '나이':26, '거주지역': '양주', '메일주소': 'he_63@nate.com',
                 '취미':('게임,목공,유튜브,요리'), '좋아하는 음식':('회, 초밥, 치킨') }
        }

for dic in dics:
        print("이름:{} / 나이:{} / 거주지역:{} / 메일주소:{} / 취미:{} / 좋아하는 음식:{}".format(dic, dics[dic]['나이'], dics[dic]['거주지역'], dics[dic]['메일주소'],
                                        dics[dic]['취미'], dics[dic]['좋아하는 음식']))