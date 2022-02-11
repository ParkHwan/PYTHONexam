while True:
    word = input("문자열을 입력하시오 :")
    wordlength = len(word)
    if 5 <= wordlength <= 8:
        continue
    elif 0 < wordlength < 5:
        result = "*" + word + "*"
        print("유효한 입력 결과 :", result) # print 함수 줄이기 삭제 가능
    elif wordlength > 8:
        result = "$" + word + "$"
        print("유효한 입력 결과 :", result) # print 함수 삭제 가능
    else:
        break
    # print("유효한 입력 결과 :", result) 하면 print 함수 하나로 호출 가능
