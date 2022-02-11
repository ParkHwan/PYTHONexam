from bs4 import BeautifulSoup

html = """
    <html>
    <head>
        <title>파이썬 웹 크롤링</title>
    </head>
    <body>
        <h1 id="title" class="hello">안녕하세요~~~</h1>
        <p id="name">박 환 입니다.</p>
    </body>
    </html>
"""

soup = BeautifulSoup(html, "html.parser")

title = soup.select_one("h1.hello")
t1 = soup.select_one("p#name")

print(f"title : {title.string}")
print(f"name : {t1.string}")