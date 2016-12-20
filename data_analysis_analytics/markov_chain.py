import numpy as np
P = 100  # maximum population size
a = .005  # birth rate
b = .005  # death rate

T = 1000 #time
x = np.zeros(T)
x[0] = 25
x[:20]


#simulate population

for t in range(T - 1):
    if 0 < x[t] < P-1:
        # Is there a birth?
        birth = np.random.rand() <= a*x[t]
        # Is there a death?
        death = np.random.rand() <= b*x[t]
        # We update the population size.
        x[t+1] = x[t] + 1*birth - 1*death
    # The evolution stops if we reach $0$ or $N$.
    else:
        x[t+1] = x[t]