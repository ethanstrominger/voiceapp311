# passed a dict with {'x': ..., 'y': ...}
# from get_ward_precinct_info
from pprint import pprint

import requests

# base_url = "https://services.arcgis.com/sFnw0xNflSi8J0uh/ArcGIS/rest/services/Precincts_2017/FeatureServer/0/query"
grocery_url = "https://services.arcgis.com/sFnw0xNflSi8J0uh/ArcGIS/rest/services/Supermarkets_GroceryStores/FeatureServer/0/query"

# lat_lon_coordinates = {'x': -71.07199821233186, 'y': 42.35156393202133}
#
# grocery_story_coordinates = {"x": -7919027.0821751533, "y": 5215208.1759242024}

ESRI_SPATIAL_REFERENCE = 3857

LAT_LONG_SPATIAL_REFERENCE = 4326

star_market_esri = {'x': -7912519.379350758, 'y': 5213279.94167787}
star_market_lon_lat = {'x': -71.0793703469, 'y': 42.3481798771}
trader_joe_lon_lat = {'x': -71.0841200722, 'y': 42.3485000974}

params = {
    "f": "json",
    "geometry": str(trader_joe_lon_lat['x']) + "," + str(trader_joe_lon_lat['y']),
    "geometryType": "esriGeometryPoint",
    "returnGeometry": "false",
    "inSR": "{}".format(LAT_LONG_SPATIAL_REFERENCE),
    "outFields": "*",
    "distance": "0.1",
    "units": "esriSRUnit_StatuteMile"
}

response = requests.request("GET", grocery_url, params=params)

pprint(response.json())

print(isinstance(response.json(), dict))
