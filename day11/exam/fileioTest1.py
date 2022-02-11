f = open("live.txt", "wt", encoding="UTF-8")  # 파일 쓰고 읽을 시 인코딩 된 값은 utf-8을 사용하도록 한다.
print(f, type(f))
f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
f.close()




