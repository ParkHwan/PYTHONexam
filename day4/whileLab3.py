import random
count = 0 # None -> False, True와 값은 데이터 값을 가지는 리터럴
while True:
    munja = 0
    number = random.randint(0, 30)
    if number < 27:
        munja = number + 64
        print(chr(munja), "(", number, ")", sep="")
        count += 1
    else:
        print("수행횟수는", count, "번입니다.")
        break
