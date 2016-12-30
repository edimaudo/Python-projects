"""
learn about apis using open notify api
goal: explore api and find number of people in space
"""
import sys
import requests
import json

# Make a get request to get the latest position of the international space station from the opennotify api.
try:
	response = requests.get("http://api.open-notify.org/iss-now.json")

	# Print the status code of the response.
	#print(response.status_code)

	#set up lat and long for Toronto
	parameters = {"lat": 43.65, "lon": -79}

	# get api data
	# Make a get request with the parameters.
	#response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

	# Print the content of the response (the data the server returned)
	#print(response.content)

	# Get the response data as a python object.  Verify that it's a dictionary.
	#data = response.json()
	#print(type(data))
	#print(data)

	#find number of people in space
	# Get the response from the API endpoint.
	response = requests.get("http://api.open-notify.org/astros.json")
	data = response.json()

	#people are currently in space.
	print(data["number"])
	#print(data)
except:
	e = sys.exc_info()
	print(e)
	sys.exit()