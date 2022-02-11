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

# 태그 안 텍스트 추출
for x in list:
    text = x.string
    print(text)

