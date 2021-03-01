import os
file_path = '/home/andrey/Python/Scripts/123.txt'
with open('123.txt', 'r+') as f:
	read_data = f.read()
	read_data = read_data.replace('dv', 'sss')
	read_data = read_data.replace('se', 'eee')
with open('321.txt', 'w') as f:
	f.write(read_data)

os.remove(file_path)
os.rename('321.txt','123.txt')
