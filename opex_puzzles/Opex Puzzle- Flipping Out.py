import math
import random
import sys

def generate_random(alist):
    return random.randint(0,len(alist)-1)

def main():
	try:
		startInfo = [0,1]
		print(generate_random(startInfo))
	except:
		e = sys.exc_info()
		print(e)

if __name__ == "__main__":
	main()