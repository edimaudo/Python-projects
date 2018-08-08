import sys
import csv
import io

def calculate_score(value):
	newvalue = value.split(",")
	if len(newvalue) < 2:
		return "Student Number: " + str(newvalue[0]) + "  " + "Total Marks: 0"
	else:
		sumvalue = newvalue[1:]
		suminfo = 0
		for value in sumvalue:
			suminfo += int(value)
		return "Student Number: " + str(newvalue[0]) + "  " + "Total Marks: " + str(suminfo)
	

def main():
	try:
		rowinfo = []
		with open('student_marks.txt', 'r') as txtfile:
			for row in txtfile:
				row = row.rstrip("\r\n")
				rowinfo.append(calculate_score(row))
				#print(calculate_score(row))
		with open('index.csv', 'a') as csv_file:  
			writer = csv.writer(csv_file)
			for info in rowinfo:
				writer.writerow([info])
	except:
		e = sys.exc_info()
		print(e)
		sys.exit(1)


if __name__ == "__main__":
	main()


#sample output
# Student Number:S1234	Total Marks:6
# Student Number:S2345	Total Marks:31
# Student Number:S3456	Total Marks:33
# Student Number:S4567	Total Marks:0
# Student Number:S5678	Total Marks:5
