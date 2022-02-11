class Member:
    def __init__(self, name, account, passwd, birthyear):
        self.name = name
        self.account = account
        self.passwd = passwd
        self.birthyear = birthyear

mems1 = Member("둘리", "아기공룡", 1234, 1004)
mems2 = Member("또치", "빨간콩", 5678, 1894)
mems3 = Member("마이클", "깜둥이", 9012, 1912)

print(f"회원 1: {mems1.name}({mems1.account},{mems1.passwd},{mems1.birthyear})")
print(f"회원 2: {mems2.name}({mems2.account},{mems2.passwd},{mems2.birthyear})")
print(f"회원 3: {mems3.name}({mems3.account},{mems3.passwd},{mems3.birthyear})")