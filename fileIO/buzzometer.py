import csv
import re
import io

def combine_data(listdata):
	if len(listdata) > 1:
		return "'" + listdata[0] + "'" + "," + "'" + listdata[1].strip() + "'"
	return "'" + listdata[0] + "'"

updated_urls = []
updated_word = ""
with open('buzzometer-31_10.csv', 'r') as csvfile:
	for row in csvfile:
		datarow = row.split(",")
		updated_word = combine_data(datarow)
		#updated_word = "'" + row + "'"
		updated_urls.append(updated_word)


with open('buzzometer.csv', 'a') as csv_file:  
	writer = csv.writer(csv_file)
	for info in updated_urls:
		writer.writerow([info])
#print(updated_urls[1])
