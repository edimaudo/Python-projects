import sys
import os

path = "" # insers your own path e.g. /users/Edima/
try:
	fileList = os.listdir(path)
	for fileName in fileList:
		print (fileName)
except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)