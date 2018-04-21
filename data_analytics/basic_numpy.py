import numpy as np

b = np.array([6, 7, 8])
type(b)

a = np.arange(10,30,5)
b = np.arange(0,10,0.01)
#b.shape
a = np.arange(15).reshape(3, 5)
print a
b = np.arange(15).reshape(5, 3)
a = np.arange(15).reshape(3, 5)
print b
print b.transpose()