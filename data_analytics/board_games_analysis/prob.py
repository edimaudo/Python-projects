import random
def coin_trial():
    heads = 0
    for i in range(100):
        if random.random() <= 0.5:
            heads +=1
    return heads

def simulate(n):
   trials = []
   for i in range(n):
       trials.append(coin_trial())
   return(sum(trials)/n)

print(simulate(10))
print(simulate(100))
print(simulate(1000))
print(simulate(10000))
print(simulate(100000))
print(simulate(1000000))