
def main():
	for value in range(1000000000000000,100000000000000000):
		valueLength = len(str(value))
		valueSquared = value**2
		if str(value) == str(valueSquared)[-valueLength:][::-1]:
			print(value)


if __name__ == "__main__":
	main()