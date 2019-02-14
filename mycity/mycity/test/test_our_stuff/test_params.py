import unittest

from mycity.mycity.test.test_our_stuff.test_long_lat import LongLatPoint

# TODO: Remove duplication, also in test_grocery_store_intent, 4326 duplicated
# TODO: Add distance and outfields as optional parameters - to be decided if part of __init__ or not
from mycity.mycity.test.test_our_stuff.test_distance import Distance, Mile


class ArcGisParams(object):
    _LAT_LONG_SPATIAL_REFERENCE = 4326
    _MILE_UNIT = "esriSRUnit_StatuteMile"

    def __init__(self, origin: LongLatPoint, distance: Distance = Mile(0.001)):
        self.origin = origin
        self.url_param = {
            "f": "json",
            "inSR": self._LAT_LONG_SPATIAL_REFERENCE,
            "geometry": f"{self.origin.x},{self.origin.y}",
            "geometryType": "esriGeometryPoint",
            "returnGeometry": "false",
            "outFields": "*",
            "distance": distance.mile,
            "units": self._MILE_UNIT
        }


    def url_params(self):
        return self.url_param


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
            "distance": 0.001,
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
        distance = Mile(miles)
        params = ArcGisParams(origin, distance)
        actual_params = params.url_params()
        self.assertEqual(expected_params, actual_params)
