# passed a dict with {'x': ..., 'y': ...}
# from get_ward_precinct_info
from pprint import pprint

import requests

base_url = "https://services.arcgis.com/sFnw0xNflSi8J0uh/ArcGIS/rest/services/Precincts_2017/FeatureServer/0/query"
grocery_url = "https://services.arcgis.com/sFnw0xNflSi8J0uh/ArcGIS/rest/services/Supermarkets_GroceryStores/FeatureServer/0/query"

coordinates = {'x': -71.07199821233186, 'y': 42.35156393202133}

grocery_story_coordinates = {"x": -7919027.0821751533, "y": 5215208.1759242024}

params = {
    "f": "json",
    "geometry": str(grocery_story_coordinates['x']) + "," + str(grocery_story_coordinates['y']),
    "geometryType": "esriGeometryPoint",
    "returnGeometry": "false",
#    "outFields": "*",
    "outFields": "Store, Address, Type, Lat, Lon, Neighborho",
    "distance": "0.5",
    "units": "esriSRUnit_StatuteMile"
}

response = requests.request("GET", grocery_url, params=params)

pprint(response.json())

print(isinstance(response.json(), dict))
