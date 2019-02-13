"""
get xy coordinates for address.  returns json with list of locations, x,y, score etc...
"""
from pprint import pprint

import requests

import mycity.utilities.arcgis_utils as au

address = '399 Boylston st., Boston, MA'
params = {'f': 'json', 'singleLine': address, 'outFields': '*', 'geometry': 'true'}

test_answer = requests.get(au.ARCGIS_GEOCODE_URL, params=params)

pprint(test_answer.json())

query_url = "https://services.arcgis.com/sFnw0xNflSi8J0uh/ArcGIS/rest/services/Precincts_2017/FeatureServer/0/query"
