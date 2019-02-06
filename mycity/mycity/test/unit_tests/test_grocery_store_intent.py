import unittest
from typing import List, Dict

import requests

"""
{'features': [{'attributes': {'Address': '370 Western Avenue',
                              'Lat': 42.3609803747,
                              'Lon': -71.137830016,
                              'Neighborho': 'Allston',
                              'Store': 'Star Market',
                              'Type': 'Supermarket'}},
              {'attributes': {'Address': '60 Everett Street',
                              'Lat': 42.3565404365,
                              'Lon': -71.1392297503,
                              'Neighborho': 'Allston',
                              'Store': 'Super Stop & Shop',
                              'Type': 'Supermarket'}},
              {'attributes': {'Address': '424 CAMBRIDGE ST',
                              'Lat': 42.3544598312,
                              'Lon': -71.1344004323,
                              'Neighborho': 'Allston',
                              'Store': 'Bazaar on Cambridge St',
                              'Type': 'Supermarket'}}]

"""

# TODO use below to create days agenda and look for things to add to list

# TODO review all function and variable names up to this point.
# TODO review code logic
# TODO discuss using mocks for "requests"
# TODO error_handling response.status_code != 200
# TODO error_handling response.json()['features'] == []


def get_grocery_store_api_response(xy_coordinates: dict) -> List[Dict]:
    grocery_url = "https://services.arcgis.com/sFnw0xNflSi8J0uh/ArcGIS/rest/services/Supermarkets_GroceryStores/FeatureServer/0/query"

    params = {
        "f": "json",
        "geometry": str(xy_coordinates['x']) + "," + str(xy_coordinates['y']),
        "geometryType": "esriGeometryPoint",
        "returnGeometry": "false",
        "outFields": "Store, Address, Type, Lat, Lon, Neighborho",
        "distance": "0.5",
        "units": "esriSRUnit_StatuteMile"
    }
    response = requests.request("GET", grocery_url, params=params)
    return response.json()['features']


ACTUAL_BOSTON_GROCERY_STORE_COORDINATES = {"x": -7919027.0821751533, "y": 5215208.1759242024}


class TestGroceryStoreIntent(unittest.TestCase):
    # def setUp(self):
    #     self.test_request = MyCityRequestDataModel()

    def test_get_grocery_store_api_response(self):
        response = get_grocery_store_api_response(ACTUAL_BOSTON_GROCERY_STORE_COORDINATES)
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)

    def test_get_grocery_store_api_response_has_correct_attributes(self):
        attribute_element_keys = sorted(('Address',
                                         'Lat',
                                         'Lon',
                                         'Neighborho',
                                         'Store',
                                         'Type'))
        response = get_grocery_store_api_response(ACTUAL_BOSTON_GROCERY_STORE_COORDINATES)
        first_json_element = response[0]
        attributes = first_json_element['attributes']
        attributes_keys = sorted(attributes.keys())
        self.assertEqual(attribute_element_keys, attributes_keys)

    # def test_get_grocery_store_locations(self):
    #
    #     locations = get_grocery_store_locations(self.test_request)
    #     expected = []
