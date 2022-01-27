import csv
import re

wordData = ""
with open('file.txt', 'r') as txtfile:
	for row in txtfile:
		for word in row:
			wordData+=word


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

positionData = list(find_all(wordData, '$'))


wordInfo = []
previousPosition = 0
for value in positionData:
	wordInfo.append(wordData[previousPosition:value+9])
	previousPosition = value + 9




# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:  
	writer = csv.writer(csv_file)
	for info in wordInfo:
		writer.writerow([info])
	

		