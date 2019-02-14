import unittest


class LongLatPoint(object):
    def __init__(self, long: float, lat: float):
        self._long = long
        self._lat = lat

    @property
    def long(self):
        return self._long

    @property
    def lat(self):
        return self._lat

    @property
    def x(self):
        return self._long

    @property
    def y(self):
        return self._lat


class TestLongLatPoint(unittest.TestCase):
    def test_init(self):
        long = 30.123
        lat = 60.123
        point = LongLatPoint(long, lat)
        self.assertEqual(point.long, long)
        self.assertEqual(point.lat, lat)

    def test_xy_properties(self):
        long = 30.123
        lat = 60.123
        point = LongLatPoint(long, lat)
        self.assertEqual(point.x, long)
        self.assertEqual(point.y, lat)