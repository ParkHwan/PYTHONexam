f = None
count = 0
try:
    f = open("yesterday.txt", "rt", encoding="UTF-8")
    for line in f:
        x = line.lower()
        if "yesterday" in x:
            count += 1
except FileNotFoundError:
    print("파일을 읽을 수 없어요")
else:
    print(f"Number of a Word 'Yesterday'{count}")
finally:
    print("수행완료!!")
