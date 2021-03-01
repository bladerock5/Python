import glob, os

spisok = os.chdir(path='\\\\msk02daascl02\\Profile\\')
for file in glob.glob("*.old"):
    print(file)