import unittest
# from mycity.utilities.arcgis_utils import get
from typing import List, Dict

import requests

from mycity.mycity.test.test_our_stuff.test_distance import Mile
# import mycity.test.test_our_stuff.test_long_lat
from mycity.mycity.test.test_our_stuff.test_long_lat import LongLatPoint


ARCGIS_GROCERY_URL = "https://services.arcgis.com/sFnw0xNflSi8J0uh/ArcGIS/rest/services/Supermarkets_GroceryStores/FeatureServer/0/query"

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
# TODO: Complete other parts of the flow from the Google doc (address stuff and forming the voice response)
# TODO review code logic
# TODO distance as a parameter to get_grocery_store_api_response
# TODO discuss using mocks for "requests"
# TODO error_handling response.status_code != 200
# TODO error_handling response.json()['features'] == []


def get_grocery_store_api_response(xy_coordinates: dict) -> List[Dict]:
    """

    :param xy_coordinates: esriGeometryPoint is NOT lat/lon
    :return:
    """
    # access_token = generate_access_token()
    grocery_url = ARCGIS_GROCERY_URL
    # grocery_token_url = "https://services.arcgis.com/ArcGIS/rest/services/Supermarkets_GroceryStores/FeatureServer/0/query"

    distance = "0.5"
    params = {
        "f": "json",
        # "token": access_token,
        "geometry": f"{xy_coordinates['x']},{xy_coordinates['y']}",
        "geometryType": "esriGeometryPoint",
        "returnGeometry": "false",
        "outFields": "Store, Address, Type, Lat, Lon, Neighborho",
        "distance": distance,
        "units": "esriSRUnit_StatuteMile"
    }
    response = requests.request("GET", grocery_url, params=params)
    return response.json()['features']


def get_stripped_api_response(initial_response):
    return [element['attributes'] for element in initial_response]


def get_add_distances_to_api_response(origin, grocery_store_api_response):
    pass


############################################################################ TESTS START HERE

ACTUAL_BOSTON_GROCERY_STORE_ESRI_COORDINATES = {"x": -7919027.0821751533, "y": 5215208.1759242024}

ACTUAL_BOSTON_GROCERY_STORE_LONGLAT_COORDINATES = (-71.0793703469, 42.3481798771)
LAT_LONG_SPATIAL_REFERENCE = 4326


class ArcGisGroceryRequest(object):
    ARCGIS_MILE_UNIT = "esriSRUnit_StatuteMile"
    ARC_GIS_URL = "https://services.arcgis.com/sFnw0xNflSi8J0uh/ArcGIS/rest/services/Supermarkets_GroceryStores/FeatureServer/0/query"

    def __init__(self, origin_point: LongLatPoint):
        self._origin_point = origin_point

    def get_nearby(self, distance):
        params = {
            "f": "json",
            "inSR": LAT_LONG_SPATIAL_REFERENCE,
            "geometry": f"{self._origin_point.x},{self._origin_point.y}",
            "geometryType": "esriGeometryPoint",
            "returnGeometry": "false",
            "outFields": "Store, Address, Type, Lat, Lon, Neighborho",
            "distance": distance.value,
            "units": self.ARCGIS_MILE_UNIT
        }
        response = requests.get(self.ARC_GIS_URL, params=params)
        return response.json()['features']


class TestGroceryStoreIntent(unittest.TestCase):
    # def setUp(self):
    #     self.test_request = MyCityRequestDataModel()

    def test_get_grocery_store_api_response(self):
        origin_point = LongLatPoint(*ACTUAL_BOSTON_GROCERY_STORE_LONGLAT_COORDINATES)
        grocery_request = ArcGisGroceryRequest(origin_point)
        miles = Mile(0.5)
        response = grocery_request.get_nearby(miles)
        print(response)
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)

    def test_get_grocery_store_api_response_has_correct_attributes(self):
        expected_attribute_keys = sorted(('Address',
                                          'Lat',
                                          'Lon',
                                          'Neighborho',
                                          'Store',
                                          'Type'))
        response = get_grocery_store_api_response(ACTUAL_BOSTON_GROCERY_STORE_ESRI_COORDINATES)
        first_json_element = response[0]
        actual_attributes = first_json_element['attributes']
        actual_attribute_keys = sorted(actual_attributes.keys())
        self.assertEqual(expected_attribute_keys, actual_attribute_keys)

    def test_get_stripped_api_response(self):
        initial_response = [{'attributes': {'test': 'other_thing'}},
                            {'attributes': {'test': 'thing'}}]
        expected = [{'test': 'other_thing'}, {'test': 'thing'}]
        actual = get_stripped_api_response(initial_response)
        self.assertEqual(expected, actual)

    @unittest.skip
    def test_get_add_distances_to_api_response(self):
        # Test is that distance is added to the grocery store api response with a number to both records
        mock_origin = ACTUAL_BOSTON_GROCERY_STORE_ESRI_COORDINATES
        mock_grocery_store_api_response = [
            {'Address': '370 Western Avenue',
             'Lat': 42.3609803747,
             'Lon': -71.137830016,
             'Neighborho': 'Allston',
             'Store': 'Star Market',
             'Type': 'Supermarket'},
            {'Address': '60 Everett Street',
             'Lat': 42.3565404365,
             'Lon': -71.1392297503,
             'Neighborho': 'Allston',
             'Store': 'Super Stop & Shop',
             'Type': 'Supermarket'}
        ]

        expected_result = [
            {'Address': '370 Western Avenue',
             'Lat': 42.3609803747,
             'Lon': -71.137830016,
             'Neighborho': 'Allston',
             'Store': 'Star Market',
             'Type': 'Supermarket',
             'Distance': 0},
            {'Address': '60 Everett Street',
             'Lat': 42.3565404365,
             'Lon': -71.1392297503,
             'Neighborho': 'Allston',
             'Store': 'Super Stop & Shop',
             'Type': 'Supermarket',
             'Distance': 1.46}
        ]
        actual_result = get_add_distances_to_api_response(mock_origin, mock_grocery_store_api_response)
        self.assertEqual(expected_result, actual_result)

    # def test_get_grocery_store_locations(self):
    #
    #     locations = get_grocery_store_locations(self.test_request)
    #     expected = []
