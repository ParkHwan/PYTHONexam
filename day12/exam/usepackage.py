import sys
sys.path.append("C:/PyStudy")
print(sys.path)

import mypack.calc.add
mypack.calc.add.outadd(1,2)

import mypack.report.table
mypack.report.table.outreport()


import mypack.calc.add as my1
my1.outadd(1,2)

import mypack.report.table as my2
my2.outreport()

from mypack.calc import add
add.outadd(1,2)

from mypack.calc import add as unico
unico.outadd(1,2)
'''
from mypack.calc import *
add.outadd(1,2)
multi.outmulti(10,20)
'''
