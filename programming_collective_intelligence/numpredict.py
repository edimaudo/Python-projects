from random import random,randint
import math
def wineprice(rating,age):
	peak_age=rating-50
	# Calculate price based on rating
	price=rating/2
	if age>peak_age:
	# Past its peak, goes bad in 5 years
		price=price*(5-(age-peak_age))
	else:
	# Increases to 5x original value as it
	# approaches its peak
	price=price*(5*((age+1)/peak_age))
	
	if price<0: price=0
	return price