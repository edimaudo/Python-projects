import pandas as pd

filenames = ['file1.csv', 'file2.csv', 'file3.csv']

results = []
for filename in filenames:
    results.append(pd.read_csv(filename))

combined = pd.concat(results, ignore_index=True)
combined.to_excel('result.xlsb', index=False)
