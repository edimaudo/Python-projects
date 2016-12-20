

def main():
	data = {"seasons":
	{
	"4":{"ncsa":{"wins":48,"losses":36,"abandons":0,"season":4,"region":"ncsa","ranking":{"rating":3397.113763,"next_rating":3400.0,"prev_rating":3200.0,"mean":33.97113763,"stdev":4,"rank":18}}},
	"3":{"ncsa":{"wins":152,"losses":162,"abandons":2,"season":3,"region":"ncsa","ranking":{"rating":4951.80855299,"next_rating":5160.0,"prev_rating":4900.0,"mean":28.3858273058,"stdev":2,"rank":17}}},
	"2":{"ncsa":{"wins":41,"losses":26,"abandons":2,"season":2,"region":"ncsa","ranking":{"rating":4419.66098484,"next_rating":4640.0,"prev_rating":4400.0,"mean":30.0860547181,"stdev":5,"rank":15}}}
	}
	}

	print(data['seasons']['4']['ncsa']["ranking"]["rank"])


if __name__ == "__main__":
	main()