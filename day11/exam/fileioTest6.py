# =============== listdir  =============== c:\\Temp 디렉토리 만들고
import os

files = os.listdir("c:\ph\PYTHONexam")  # \\, \, / 는 디렉토리 구분자
print(type(files))
for f in files:
    print(f)

# =============== listdir2  ===============
print("-+"*20)
import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = path + "\\" + f
        if os.path.isdir(fullpath):
            print("[" + fullpath + "]")
            dumpdir(fullpath)
        else:
            print("\t" + fullpath)

dumpdir("c:\ph\PYTHONexam")
