import xlwt
import xlrd

wkbk = xlwt.Workbook()
outsheet = wkbk.add_sheet('Sheet1')

xlsfiles = [r'C:\foo.xlsx', r'C:\bar.xlsx', r'C:\baz.xlsx']

outrow_idx = 0
for f in xlsfiles:
    # This is all untested; essentially just pseudocode for concept!
    insheet = xlrd.open_workbook(f).sheets()[0]
    for row_idx in xrange(insheet.nrows):
        for col_idx in xrange(insheet.ncols):
            outsheet.write(outrow_idx, col_idx, 
                           insheet.cell_value(row_idx, col_idx))
        outrow_idx += 1
wkbk.save(r'C:\combined.xls')

#if each file has a header then update the above code
#firstfile = True # Is this the first sheet?
#for f in xlsfiles:
#    insheet = xlrd.open_workbook(f).sheets()[0]
#    for row_idx in xrange(0 if firstfile else 1, insheet.nrows):
#        pass # processing; etc
#    firstfile = False # We're done with the first sheet.