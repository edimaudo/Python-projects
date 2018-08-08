import sys
import csv
import io

def main():
	try:
		#do something
		with open('student_marks.txt', 'r') as txtfile:

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
