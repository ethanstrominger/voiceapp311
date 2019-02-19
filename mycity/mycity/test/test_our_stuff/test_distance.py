import unittest

from mycity.test.test_our_stuff.distance import Distance


class TestDistance(unittest.TestCase):


    def test_from_kilometers_to_kilometers(self):
        value = 3.0
        distance = Distance.from_kilometers(value)
        self.assertEqual(distance.kilometers, value)
#

    def test_from_kilometers_to_miles(self):
        kilometer_value = 1.60934
        distance = Distance.from_kilometers(kilometer_value)
        mile_value = distance.miles
        self.assertAlmostEqual(mile_value, 1.0, places=4)

    def test_from_miles_to_miles(self):
        value = 3.0
        distance = Distance.from_miles(value)
        self.assertEqual(distance.miles, value)
#

    def test_from_miles_to_kilometers(self):
        mile_value = 1.0
        distance = Distance.from_miles(mile_value)
        kilometer_value = distance.kilometers
        self.assertAlmostEqual(kilometer_value, 1.60934, places=4)


