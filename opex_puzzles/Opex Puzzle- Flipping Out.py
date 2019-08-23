import math
import random
import sys

def generate_random(alist):
    return random.randint(0,len(alist)-1)

def main():
	try:
		player1 = []
		player2 = []
		flipInfo = [0,1]
		for value in range(0,100000):
			endGame = True
			while (endGame):
				if generate_random(flipInfo) == 0:
					player1.append(1)
					player2.append(0)
					endGame = False
				if generate_random(flipInfo) == 0:
					player2.append(1)
					player1.append(0)
					endGame = False
		print("player 1 win rate is: " + str(sum(player1)/100000.0))
		print("player 2 win rate is: " + str(sum(player2)/100000.0))
	except:
		e = sys.exc_info()
		print(e)

if __name__ == "__main__":
	main()