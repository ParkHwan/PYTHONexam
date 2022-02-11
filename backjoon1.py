"""import sys

T = int(input()) #Test case
for i in range(T):
        a,b = map(int, sys.stdin.readline().split())
        print(a+b)

help(sys)
"""
"""stock = 0
def GoodStock():
    global stock
    code = input("상품 코드를 입력하세요: ")
    stock = int(input("재고 수량을 입력하세요: "))
    print(f"상품 코드 : {code}")
    print(f"재고 수량 : {stock}")

def addStock():
    add = int(input("추가할 수량을 입력하세요 :"))
    newstock = stock + add
    print(f"재고 수량 : {newstock}")

GoodStock()
addStock()

class GoodStock:
    def __init__(self, code, stock):
        self.code = code
        self.stock = stock
    def addStock(self, add):
        self.stock += add

code = input("상품 코드를 입력하세요 :")
stock = int(input("재고 수량을 입력하세요 :"))
obj = GoodStock(code, stock)
print(f"상품 코드 : {obj.code}")
print(f"재고 수량 : {obj.stock}")
add = int(input("추가할 수량을 입력하세요 :"))
obj.addStock(add)
print(f"재고 수량 : {obj.stock}")
"""
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

print(f"h1 : {h1.string}")
print(f"p : {p.string}")
