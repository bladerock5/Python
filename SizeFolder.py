import win32com.client as com

path='\\\\msk02daascl02\\Profile\\naumovav'
fso = com.Dispatch("Scripting.FileSystemObject")
folder = fso.GetFolder(path)
mb=1024*1024.0
a="{}".format(folder.Size/mb)
print(a)