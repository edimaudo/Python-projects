import csv
import codecs
import io

wordCounter = {}
with open('sample.csv', 'r') as csvfile:
	 sample = csv.reader(csvfile, delimiter=',', quotechar='|')
	 for row in sample:
	 	for word in row:
	 		if word not in wordCounter:
	 			wordCounter[word] = 1
	 		else:
	 			wordCounter[word]+=1
print(wordCounter)