from bs4 import BeautifulSoup

html = """
    <html>
    <head>
        <title>파이썬 웹 크롤링</title>
    </head>
    <body>
        <h1>안녕하세요~~~</h1>
        <p>박 환 입니다.</p>
    </body>
    </html>
"""
# html  태그 분석
soup = BeautifulSoup(html, "html.parser")

h1 = soup.html.body.h1
p = soup.html.body.p

print(h1)
print(f"h1 : {h1.string}")
print(f"p : {p.string}")
