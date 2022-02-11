f = None
try:
    f = open("live_ansi.txt", "rt") # 디폴트 encoding='cp949'
    print(f, type(f))
    text = f.read()
    print(text)
except FileNotFoundError as e:
    print("파일이 없습니다. - ", e)
except UnicodeDecodeError as e:
    print("인코딩 형식이 다르네요. -", e)
finally:
    if f :
        print("파일 닫을께요")
        f.close()
    else :
        print("열리지도 않았네요")

