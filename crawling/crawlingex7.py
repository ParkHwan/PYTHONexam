from bs4 import BeautifulSoup
import urllib.request as req

url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
# url 열기
result = req.urlopen(url)

# 데이터 분석 하기
soup = BeautifulSoup(result, "html.parser")

# title 추출하기
title = soup.find("title").string
text = soup.find("wf").string

print(title)
print(result)
print(text)