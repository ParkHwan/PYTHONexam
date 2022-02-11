class Account:
    def __init__(self, accountNo, ownerName, balance):
        self.accountNo = accountNo
        self.ownerName = ownerName
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            self.balance = " 잔액이 부족합니다"
        else:
            self.balance -= amount

def printAccount(obj):
    print(f"계좌번호 : {obj.accountNo}\n"
          f"예금주 이름 : {obj.ownerName}\n"
          f"잔액 : {obj.balance}\n")

obj1 = Account("111-222-3333333", "정수아", 50000)
obj2 = Account("555-444-9999999", "손이안", 100000)

obj1.deposit(100000)
printAccount(obj1)

obj2.withdraw(130000)
printAccount(obj2)



