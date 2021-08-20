## MOVE THIS FILE OFF GITHUB REPO BEFORE SYNCING!

# https://console.cloud.google.com/google/maps-apis/credentials?project=eloquent-vector-323516&supportedpurview=project

import googlemaps
import importlib

# api_key = "AIzaSyA-l-fuu_h49EowtjLnUc5CenUqvlWmadk"
api_key = "AIzaSyB5ZyS85-PmbX9RMb9LyQ80XncDdzVIOQE"  # Ben's API key
client = googlemaps.Client(api_key)

"""
# Testing authentication worked 
imported_items = importlib.import_module('start_google_Cecilia')

# Copy client to an object named gmaps
gmaps = imported_items.client

# Locate the white house
whitehouse = 'The White House'
location = gmaps.geocode(whitehouse)
print(location) # location is a list of dictionaries

"""