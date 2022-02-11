def myprint(*a, **b):
    if len(a) == 0 and len(b) == 0:
        print("Hello Python")
    else:
        deco = "**"
        sep = ","
        if "deco" in b:
            deco = b["deco"]
        if "sep" in b:
            sep = b["sep"]
        print(deco, end = "") # print(deco = "**", end = "")
        for i in range(len(a)):
            print(a[i], end = "")
            if i < (len(a) -1):
                print(sep, end = "")
        print(deco)


myprint(10, 20, 30, deco = "@", sep = "-")
myprint("python", "javascript", "R", deco="$")
myprint("가", "나", "다")
myprint(100)
myprint(True, 111, False, "abc", deco="&", sep="")

# funcLab13 에서 11번 줄 print(deco, end ='')을
# (deco = "**", end = "")로 디폴트 값을 주고
# 하면 왜 안되는걸까요?

help(dict)