class Member:
    def __init__(self, name, account, passwd, birthyear):
        self.name = name
        self.account = account
        self.passwd = passwd
        self.birthyear = birthyear

members = [
    Member("둘리", "아기공룡", 1234, 1004),
    Member("또치", "빨간콩", 5678, 1894),
    Member("마이클", "깜둥이", 9012, 1912)
    ]

for i, people in enumerate(members, 1):
    print(f"회원{i}:{people.name}({people.account},{people.passwd},{people.birthyear})")