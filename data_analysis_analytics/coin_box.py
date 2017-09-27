import random




def checkbox():
	count = 0
	randbox = random.randint(0,2)
	randcompartment = random.randint(0,2)
	info = [['b1',[1,1]],['b2',[0,0]],['b3',[0,1]]]
	yescheck = 0
	while count < 10001:
		randbox = random.randint(0,2)
		if info[randbox][1][0] == 0 and info[randbox][1][1] == 1:
			yescheck+=1
		count+=1
	print(yescheck/10000.00)


def main():
	checkbox()

if __name__ == "__main__":
	main()

