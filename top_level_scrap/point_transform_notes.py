import unittest
from collections import namedtuple

from pyproj import Proj, transform

ESRI_SPATIAL_REFERENCE = 3857

LAT_LONG_SPATIAL_REFERENCE = 4326

LongLat = namedtuple("LongLat", ("long", "lat"))

# TODO: Force type of argument values
# TODO: Look for other refactorings
# TODO: Add functionality to convert to ESRI
# TODO: Add type hinting every where

# TODO https://esri.github.io/arcgis-python-api/apidoc/html/arcgis.geometry.html#project


class MyCityPoint(object):
    def __init__(self, x, y, spatial_reference):
        self.x = x
        self.y = y
        self.spatial_reference = spatial_reference

    @classmethod
    def long_lat(cls, long, lat) -> 'MyCityPoint':
        return cls(x=long, y=lat, spatial_reference=LAT_LONG_SPATIAL_REFERENCE)

    @classmethod
    def esri(cls, x, y) -> 'MyCityPoint':
        return cls(x, y, ESRI_SPATIAL_REFERENCE)

    def get_long_lat(self) -> LongLat:
        long, lat = self.convert_point(LAT_LONG_SPATIAL_REFERENCE)
        return LongLat(long, lat)

    def convert_point(self, spatial_reference):
        if spatial_reference == self.spatial_reference:
            return self.x, self.y
        in_proj = Proj(init='epsg:{}'.format(self.spatial_reference))
        out_proj = Proj(init='epsg:{}'.format(spatial_reference))
        answer = transform(in_proj, out_proj, self.x, self.y)
        print(answer)
        return answer


class TestPoint(unittest.TestCase):
    def test_init(self):
        point = MyCityPoint(43, 27, 4326)
        self.assertEqual(point.x, 43)
        self.assertEqual(point.y, 27)
        self.assertEqual(point.spatial_reference, 4326)

    def test_class_method_long_lat(self):
        point = MyCityPoint.long_lat(74, 97)
        self.assertEqual(point.x, 74)
        self.assertEqual(point.y, 97)
        self.assertEqual(point.spatial_reference, LAT_LONG_SPATIAL_REFERENCE)

    def test_class_method_esri(self):
        point = MyCityPoint.esri(74, 97)
        self.assertEqual(point.x, 74)
        self.assertEqual(point.y, 97)
        self.assertEqual(point.spatial_reference, ESRI_SPATIAL_REFERENCE)

    def test_get_long_lat_from_long_lat_instantiated_point(self):
        coordinates = 12, 34
        point = MyCityPoint.long_lat(*coordinates)
        actual = point.get_long_lat()
        self.assertEqual(actual, coordinates)

    def test_get_long_lat_from_esri_instantiated_point(self):
        esri_coordinates = (-7919027.0821751533, 5215208.1759242024)

        point = MyCityPoint.esri(*esri_coordinates)
        actual = point.get_long_lat()
        expected = (-71.137830016, 42.3609803747)
        actual_x, actual_y = actual
        expected_x, expected_y = expected
        delta = 0.00001
        self.assertAlmostEqual(actual_x, expected_x, delta=delta)
        self.assertAlmostEqual(actual_y, expected_y, delta=delta)
