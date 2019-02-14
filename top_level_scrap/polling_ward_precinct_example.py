# getting
from pprint import pprint

import requests

ward = '05'
precinct = '06'
base_url = "https://services.arcgis.com/sFnw0xNflSi8J0uh/arcgis/rest/services/polling_locations_2017/FeatureServer/0/query"

params = {
    "f": "json",
    "returnGeometry": "true",
    "where": "Ward = " + ward + "AND Precinct = " + precinct,
    "outFields": "Location2, Location3, Location4"
}
response = requests.request("GET", base_url, params=params)


pprint(response.json())