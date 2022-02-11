from bs4 import BeautifulSoup
import urllib.request as req

# urlopen()함수로 기상청의 전국 날씨를 가져옴
target = req.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

# BeatifulSoup을 사용해 웹 페이지를 분석
soup = BeautifulSoup(target, "html.parser")
# location 태그를 찾는다.
for location in soup.select("location"):
    # 내부의 city, wf, tmn, tmx 태그를 찾아 출력
    print(f"도시 : {location.select_one('city').string}")
    print(f"날씨 : {location.select_one('wf').string}")
    print(f"최저기온 : {location.select_one('tmn').string}")
    print(f"최고기온 : {location.select_one('tmx').string}")
    print()