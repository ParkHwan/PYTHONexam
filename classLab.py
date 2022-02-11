class Account:
    def __init__(self, accountNo, ownerName, balance):
        self.accountNo = accountNo
        self.ownerName = ownerName
        self.balance = balance

    def deposit(self, dep):
        self.balance += dep

    def withdraw(self, wit):
        self.balance -= wit

obj1 = Account("111-222-3333333", "정수아", 50000)
obj2 = Account("555-444-9999999", "손이안", 100000)

obj1.deposit(100000)
obj2.withdraw(30000)

def printAccount():
    print(f"계좌번호 : {obj1.accountNo}\n"
          f"예금주 이름 : {obj1.ownerName}\n"
          f"잔액 : {obj1.balance}\n\n"
          f"계좌번호 : {obj2.accountNo}\n"
          f"예금주 이름 : {obj2.ownerName}\n"
          f"잔액 : {obj2.balance}\n\n"
          )

printAccount()




