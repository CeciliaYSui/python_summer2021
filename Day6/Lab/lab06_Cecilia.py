# TODO: write code to answer the following questions: 
# 1) which of these embassies is closest to the White House in meters? 
# how far is it, and what is the address?
# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
# 3) if I wanted to hold an evening meeting there, which bar would you suggest? 
# for 2 and 3, you will need to enable the google places API
# you may find this page useful to learn about different findinging nearby places https://www.geeksforgeeks.org/python-fetch-nearest-hospital-locations-using-googlemaps-api/

import importlib
import os
import googlemaps
# os.chdir('you/key/dir')
imported_items = importlib.import_module('start_google_Cecilia')
gmaps = imported_items.client

whitehouse = '1600 Pennsylvania Avenue, Washington, DC'

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

from pprint import pprint
# grab loc of whitehouse 
location = gmaps.distance_matrix(whitehouse, embassies)
emb_dict = {}
for i in range(3):
	emb = location["destination_addresses"][i]
	d = float(location["rows"][0]["elements"][i]["distance"]["text"].split()[0])
	emb_dict[emb] = d

# find minimum distance & address: 
min_val = min(emb_dict.values())
min_emb = min(emb_dict)
# Q1: 
print("Q1: \nThe closest embassy to white house is at {} with a distance of {} m.".format(min_emb, min_val*1000))


# Q2: 
# pprint(gmaps.places_nearby(embassies[1], rank_by = "distance", 
# 					type = "cafe", keyword = "breakfast"))
cafe_result = gmaps.places_nearby(embassies[1], rank_by = "distance", 
					type = "cafe", keyword = "breakfast")

# print(type(result)) # dict
cafe = cafe_result["results"][0]["name"]
print("Q2: \nBased on distance, we recommend {} cafe. ".format(cafe))

# Q3: 
# rating
bar_result = gmaps.places_nearby(embassies[1], rank_by = "distance", type = "bar")
bars = {}

for i in range(len(bar_result)):
	name = bar_result["results"][i]["name"]
	rating = bar_result["results"][i]["rating"]
	bars[name] = rating

bar_rec = max(bars, key = bars.get)
print("Q3: \nBased on ratings, we recommend {} bar. ".format(bar_rec))





