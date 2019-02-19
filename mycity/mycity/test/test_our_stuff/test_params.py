import unittest

from mycity.test.test_our_stuff.arc_gis_params import ArcGisParams
from mycity.test.test_our_stuff.distance import Distance
from mycity.test.test_our_stuff.longlat import LongLatPoint

# TODO: Remove duplication, also in test_grocery_store_intent, 4326 duplicated
# TODO: Add distance and outfields as optional parameters - to be decided if part of __init__ or not


class TestParams(unittest.TestCase):
    def test_init(self):
        origin = LongLatPoint(30.0, 45.0)
        params = ArcGisParams(origin)
        self.assertIs(params.origin, origin)

    def test_default_params(self):
        origin = LongLatPoint(30.0, 45.0)
        expected_params = {
            "f": "json",
            "inSR": 4326,
            "geometry": f"{origin.x},{origin.y}",
            "geometryType": "esriGeometryPoint",
            "returnGeometry": "false",
            "outFields": "*",
            "distance": ArcGisParams.DEFAULT_QUERY_DISTANCE,
            "units": "esriSRUnit_StatuteMile"
        }
        params = ArcGisParams(origin)
        actual_params = params.url_params()
        self.assertEqual(expected_params, actual_params)

    def test_distance_param(self):
        origin = LongLatPoint(30.0, 45.0)
        miles = 1.78
        expected_params = {
            "f": "json",
            "inSR": 4326,
            "geometry": f"{origin.x},{origin.y}",
            "geometryType": "esriGeometryPoint",
            "returnGeometry": "false",
            "outFields": "*",
            "distance": miles,
            "units": "esriSRUnit_StatuteMile"
        }
        distance = Distance.from_miles(miles)
        params = ArcGisParams(origin, distance)
        actual_params = params.url_params()
        self.assertEqual(expected_params, actual_params)


    def test_outfields_param(self):
        origin = LongLatPoint(30.0, 45.0)
        miles = 1.78
        expected_params = {
            "f": "json",
            "inSR": 4326,
            "geometry": f"{origin.x},{origin.y}",
            "geometryType": "esriGeometryPoint",
            "returnGeometry": "false",
            "outFields": "field1,field2,field3",
            "distance": ArcGisParams.DEFAULT_QUERY_DISTANCE,
            "units": "esriSRUnit_StatuteMile"
        }
        distance = Distance.from_miles(miles)
        params = ArcGisParams(origin=origin, out_fields="field1,field2,field3")
        actual_params = params.url_params()
        self.assertEqual(expected_params, actual_params)
