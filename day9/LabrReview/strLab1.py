def myemail_info (email):
    if "@" in email:
        print(email.split("@"))
    else :
        print(None)

myemail_info("power080900@naver.com")
myemail_info("power080900naver.com")


def myemail_info(s):
    if '@' not in s:
        return None
    else:
        return tuple(s.split('@'))

print(myemail_info('mesh153@naver.com'))
print(myemail_info('mesh153naver.com'))