from bs4 import BeautifulSoup

html = """
    <html>
    <head>
        <title>find_all()</title>
    </head>
    <body>
        <ul>
            <li><a href="http://www.naver.com">네이버</a></li>
            <li><a href="http://www.google.com">구글</a></li>
        </ul>
    </body>
    </html>
"""
# html  태그 분석
soup = BeautifulSoup(html, "html.parser")
list = soup.find_all("a")

# 속성값 추출
for x in list:
    #href = x.attrs["href"]
    href = x.get("href")
    print(href)

