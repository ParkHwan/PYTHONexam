import os

path = "c:\ph\WEBCLIENTexam\htmlexam\images"
files = os.listdir(path)
for f in files:
    if (f.find("_") != -1 and f.endswith(".png")):
        name = f[0:-4]
        print(name)
        ext = f[-4:]
        part = name.split("_")
        newname = part[1].strip() + "-" + part[0].strip()+"-new" + ext
        print(newname)