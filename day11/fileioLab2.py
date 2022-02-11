f = None
try:
    f = open("sample.txt", "rt", encoding="UTF-8")
    text = f.read()
    f = open("sample_yyyy_mm_dd.txt", "at", encoding="UTF-8")
    f.write(f"{text}\n\n")
finally:
    if f:
        print("저장이 완료되었습니다.")
        f.close()
