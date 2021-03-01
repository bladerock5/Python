import os
import win32com.client as com

def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
            mb = 1024 * 1024.0
            total_size2 = total_size / mb
            total_size2 = float('{:.2f}'.format(total_size2))
    return total_size2

spisok = os.listdir(path='\\\\msk02daascl02\\Profile\\')
spisok2 = []
for element in spisok:
        path1 = '\\\\msk02daascl02\\Profile\\'
        path2 = path1 + element
        spisok2.append(path2)

for path3 in spisok2:
    try:
        print(path3, get_size(path3))
    except Exception:
        print('Error')
        continue