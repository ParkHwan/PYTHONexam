"""[ 실습 3 ]
파일명 : compreLab3.py
아래 리스트 항목 중에서 소문자만 추출해서 리스트를 생성하여 listv2에 저장하고 출력한다.(리스트 컴프리헨션 사용)
listv1 = ["A", "b", "c", "D", "e", "F", "G", "h"]
"""
listv1 = ["A", "b", "c", "D", "e", "F", "G", "h"]
listv2 = [n for n in listv1 if n.islower()]
print(listv2)