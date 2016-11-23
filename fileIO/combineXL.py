
import os
import pandas as pd

path = os.getcwd()
files = os.listdir(path)

files_xls = [f for f in files if f[-3:] == 'xls'] #can be updated depending on the version of excel

#output version 1
df = pd.DataFrame()
for f in files_xls:
    data = pd.read_excel(f, 'Sheet1')
    df = df.append(data)

#output version 2
#df = []
#for f in ['c:\\file1.xls', 'c:\\ file2.xls']:
##    data = pd.read_excel(f, 'Sheet1').iloc[:-2]
#    data.index = [os.path.basename(f)] * len(data)
#    df.append(data)

#df = pd.concat(df)