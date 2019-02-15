import unittest

from mycity.test.test_our_stuff.longlat import LongLatPoint


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