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

print(list)
print(list[0])
print(list[1])

