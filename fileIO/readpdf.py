import PyPDF2
import sys
path = "/Users/edima/Desktop/"


try:
	pdf_file = open(path + 'djlist.pdf')
	read_pdf = PyPDF2.PdfFileReader(pdf_file)
	number_of_pages = read_pdf.getNumPages()
	page = read_pdf.getPage(0)
	page_content = page.extractText()
	print (page_content)
except:
	e = sys.exc_info()
	print(e)
	sys.exit(1)
