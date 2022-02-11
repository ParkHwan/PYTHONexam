from bs4 import BeautifulSoup
import urllib.request as req

# urlopen()함수로 다음 뉴스
target = req.urlopen("https://news.daum.net")

# BeatifulSoup을 사용해 웹 페이지를 분석
soup = BeautifulSoup(target, "html.parser")
# 파일로 만든다.
f = open("c:/ph/today_daum_news.txt", "wt", encoding="UTF-8")
for issue in soup.select("strong.tit_g"):
    a = issue.select_one("a")
    f.write(f"링크 : {a.get('href')}\n"
            f"제목 : {a.string.strip()}\n\n")
f.close()
print("저장이 완료되었습니다.")