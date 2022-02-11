class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def getBookInfo(self):
        return f"{self.title},{self.author},{self.price}"

    def __str__(self):
        return "Book 클래스로 생성된 객체"

objects = [
    Book("파이썬 정복", "김상형", 22000),
    Book("점프 투 장고", "박응용", 19800),
    Book("생활코딩! HTML+CSS+자바스크립트", "이고잉", 27000),
    Book("이것이 MariaDB다", "우재남", 30000),
    Book("맛있는 Mongo DB", "정승호", 28000)
    ]

for i, books in enumerate(objects, 1):
    print(f"[ 객체{i}:{str(books)} ]")
    print(f"책이름: {books.title}\n저자: {books.author}\n가격: {books.price}")
    print("-" * 70)


