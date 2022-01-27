filepath = 'rosalind_ini5.txt' 
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
   	if cnt % 2 == 0:
   		print(line)
   		cnt+=1

