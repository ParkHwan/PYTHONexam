from bs4 import BeautifulSoup

html = """
    <html>
    <head>
        <title>파이썬 웹 크롤링</title>
    </head>
    <body>
        <h1 id="title">안녕하세요~~~</h1>
        <p id="name">박 환 입니다.</p>
    </body>
    </html>
"""
# html  태그 분석
soup = BeautifulSoup(html, "html.parser")

title = soup.find("h1")
name = soup.find("p")

print(f"title : {title.string}")
print(f"name : {name.string}")
