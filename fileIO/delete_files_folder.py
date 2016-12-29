import os
import sys

dirPath = "/home/giu/pyExperiments/toRemove"
try:
	fileList = os.listdir(dirPath)
	for fileName in fileList:
		os.remove(dirPath+"/"+fileName)
except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)