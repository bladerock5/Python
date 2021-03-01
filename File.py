import os

p = "c:\\temp\\III.ps1"
f = open(p, 'w')
f.write(p)
f.close()

#os.system("(powershell -file c:\\temp\\III.ps1)")