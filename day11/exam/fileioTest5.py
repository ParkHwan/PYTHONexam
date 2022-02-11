# =============== filecopy  ===============
import shutil
import os
print(os.getcwd())

if os.path.exists("live2.txt") :
   print("파일이 존재합니다.")
else :
   print("파일이 존재하지 않습니다.")

print("[ 파일 복사 ]")
shutil.copy("live.txt", "live2.txt")
if os.path.exists("live2.txt") :
   print("파일이 존재합니다.")
else :
   print("파일이 존재하지 않습니다.")

help(os.path)