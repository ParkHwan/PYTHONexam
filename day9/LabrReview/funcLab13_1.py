def myprint(*p,**args):
    if not p and not args:
        print("Hello Python")
        return
    deco = ''
    sep = ''
    strlist = []

    if "deco" not in args:
        deco = "**"
    else:
        deco = args["deco"]

    if "sep" not in args:
        sep = ','
    else:
        sep = args["sep"]

    for s in p:
        strlist.append(str(s))

    print(deco,sep.join(strlist),deco,sep='')
    #print(strlist)

myprint(10, 20, 30, deco="@", sep='-')
myprint("python","javascript","R",deco="&")
myprint("가","나","다")
myprint(100)
myprint(True,111,False,"abc",deco="&",sep="")
myprint()