import numpy as np

def main():
	mu = 15000
	sigma = 1500
	amount = 10000
	cost = 10000.00
	bid_preparation = 350
	total_cost = cost + bid_preparation
	s = np.random.normal(mu, sigma, amount)
	competitor_amount = sum(list(s))/float(amount)
	print(competitor_amount, total_cost)
	#bid between these prices




if __name__ == "__main__":
	main()