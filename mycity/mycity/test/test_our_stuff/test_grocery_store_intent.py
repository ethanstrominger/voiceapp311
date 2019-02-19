import copy
import unittest
# from mycity.utilities.arcgis_utils import get

from mycity.test.test_our_stuff.arc_gis_grocery_request import ArcGisGroceryRequest
from mycity.test.test_our_stuff.distance import Distance
from mycity.test.test_our_stuff.new_util import add_distances_to_api_response
from mycity.test.test_our_stuff.longlat import LongLatPoint

ARCGIS_GROCERY_URL = "https://services.arcgis.com/sFnw0xNflSi8J0uh/ArcGIS/rest/services/Supermarkets_GroceryStores/FeatureServer/0/query"


# TODO use below to create days agenda and look for things to add to list
# TODO: Complete other parts of the flow from the Google doc (address stuff and forming the voice response)
# TODO review code logic
# TODO distance as a parameter to get_grocery_store_api_response
# TODO discuss using mocks for "requests"
# TODO error_handling response.status_code != 200
# TODO error_handling response.json()['features'] == []


MOCK_STAR_MARKET_LONGLAT_POINT = LongLatPoint(-71.137830016, 42.3609803747)


############################################################################ TESTS START HERE

# TODO: Can we get rid of ESTRI coordinate test and just do long lat?
# ACTUAL_BOSTON_GROCERY_STORE_ESRI_COORDINATES = {"x": -7919027.0821751533, "y": 5215208.1759242024}

LAT_LONG_SPATIAL_REFERENCE = 4326


class TestGroceryStoreIntent(unittest.TestCase):
    # def setUp(self):
    #     self.test_request = MyCityRequestDataModel()

    def test_get_grocery_store_api_response(self):
        expected_attribute_keys = sorted(('Address',
                                          'Lat',
                                          'Lon',
                                          'Neighborho',
                                          'Store',
                                          'Type'))

        origin_point = MOCK_STAR_MARKET_LONGLAT_POINT
        grocery_request = ArcGisGroceryRequest(origin_point)
        miles = Distance.from_miles(0.5)
        response = grocery_request.get_nearby(miles)
        # print(response)
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        first_json_element = response[0]
        actual_attributes = first_json_element['attributes']
        actual_attribute_keys = sorted(actual_attributes.keys())
        self.assertEqual(expected_attribute_keys, actual_attribute_keys)


    def test_get_stripped_api_response(self):
        initial_response = [{'attributes': {'test': 'other_thing'}},
                            {'attributes': {'test': 'thing'}}]
        expected = [{'test': 'other_thing'}, {'test': 'thing'}]
        actual = ArcGisGroceryRequest.get_stripped_api_response(initial_response)
        self.assertEqual(expected, actual)

    def test_add_distances_to_api_response(self):
        # Test is that distance is added to the grocery store api response with a number to both records
        # Setup
        mock_origin = MOCK_STAR_MARKET_LONGLAT_POINT
        mock_grocery_store_api_response = [
            {'Address': '370 Western Avenue',
             'Lat': mock_origin.lat,
             'Lon': mock_origin.long,
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
        # make a copy of mock response which gets modified
        original_mock_grocery_store_api_response = copy.deepcopy(mock_grocery_store_api_response)

        # Add distance to the mock_grocery_store_api_response object
        add_distances_to_api_response(mock_origin, mock_grocery_store_api_response)

        # Set a variable to be copy of the new response without distance
        mock_grocery_store_api_response_without_distance = copy.deepcopy(mock_grocery_store_api_response)
        del mock_grocery_store_api_response_without_distance[0]['distance_in_miles']
        del mock_grocery_store_api_response_without_distance[1]['distance_in_miles']

        # Do the tests
        self.assertEqual(original_mock_grocery_store_api_response, mock_grocery_store_api_response_without_distance)
        self.assertEqual(mock_grocery_store_api_response[0]['distance_in_miles'],0)
        self.assertGreater(mock_grocery_store_api_response[1]['distance_in_miles'],0)
