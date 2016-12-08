from pylab import *

figure(1, figsize=(6,6))

plot([1,2,3,4,5,6,7,8,9,10], [1,4,9,16,25,36,49,64,81,100])
title('Quadratic', bbox={'facecolor':'0.8', 'pad':10})

show()

#log log

# make a square figure and axes
figure(1, figsize=(6,6))

loglog([1,2,3,4,5,6,7,8,9,10], [1,4,9,16,25,36,49,64,81,100],basex=10,basey=10)
title('LogQuadratic', bbox={'facecolor':'0.8', 'pad':10})
show()


#pie chart
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15,30,45, 10]

##  The highlights the hogs wedge, pulling it out slightly from the pie.
explode=(0, 0.05, 0, 0)
pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})

show()