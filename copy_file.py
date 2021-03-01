#Копирование файла в директорию профиля пользователя если она существует
import os
import datetime
import shutil

dir1=os.listdir(path='\\\\msk02daasCL02\\Profile\\')
for key in dir1:
    startpath='\\\\msk02daasCL02\\Profile\\'
    endpath='\\AppData\\Roaming\\Microsoft\\Internet Explorer\\Quick Launch\\User Pinned\\TaskBar\\'
    finishpath=startpath + key + endpath
    if os.path.isdir(finishpath):
        try:
            shutil.copy2('C:\\temp\\Google Chrome.lnk', finishpath)
        except OSError as e:
            error = e
            print(error.args[0],error.args[1])
            print(e)
    else:
        print ("Объект " + finishpath + " не найден")