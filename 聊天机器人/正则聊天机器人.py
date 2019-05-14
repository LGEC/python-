import re
import sys

while True:
	enter = input('主人： ')
	x = re.sub(r'你','我',enter)
	y = re.sub(r'吗','',x)
	send = re.sub(r'？','',y)
	if send=='拜拜'|send=='再见':
		print('小白：',send)
		sys.exit()
	else:
		print('小白：',send)

# AttributeError