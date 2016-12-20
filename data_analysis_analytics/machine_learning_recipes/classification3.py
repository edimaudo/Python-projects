# more classification
# understanding why good features are important
# make sure features are independent, easy to understand and not reduendant

import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height = 28 + 4 + np.random.randn(greyhounds)
lab_height = 24 + 4 + np.random.randn(labs)

plt.hist([grey_height,lab_height],stacked=True,color=['r','b'])
plt.show()