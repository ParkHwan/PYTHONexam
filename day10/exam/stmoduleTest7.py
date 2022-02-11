# =============== sys  ===============
import sys

print("버전 :", sys.version)
#sys.exit(0) # 파이썬을 강제로 종료, 숫자가 0이면 정상종료, 0이 아니면 비정상 종료
print("플랫폼 :", sys.platform)
if (sys.platform == "win32"):
    print(sys.getwindowsversion())
print("바이트 순서 :", sys.byteorder)
print("모듈 경로 :", sys.path)
#sys.exit(0)

