import unittest

from mycity.test.test_our_stuff.distance import Distance, Kilometer, Mile


class TestConversion(unittest.TestCase):
    def test_mile_to_mile(self):
        mile_value = 1.78329
        distance = Mile(mile_value)
        self.assertEqual(mile_value, distance.mile)

    def test_kilometer_to_kilometer(self):
        kilometer_value = 1.78329
        distance = Kilometer(kilometer_value)
        self.assertEqual(kilometer_value, distance.kilometer)

    def test_kilometer_to_mile(self):
        kilometer_value = 1.60934
        distance = Kilometer(kilometer_value)
        mile_value = distance.mile
        self.assertAlmostEqual(mile_value, 1.0, places=4)

    def test_mile_to_kilometer(self):
        mile_value = 2.5 / 1.60934
        distance = Mile(mile_value)
        kilometer_value = distance.kilometer
        self.assertAlmostEqual(kilometer_value, 2.5, places=4)


import unittest


class TestMile(unittest.TestCase):

    def test_init(self):
        value = 3.0
        distance = Mile(value)
        self.assertEqual(distance.value, value)

    def test_kilometer_to_mile(self):
        kilometer_value = 1.60934
        distance = Kilometer(kilometer_value)
        mile_value = distance.mile
        self.assertAlmostEqual(mile_value, 1.0, places=4)

    def test_is_subclass_of_Distance(self):
        value = 3.0
        distance = Mile(value)
        self.assertIsInstance(distance, Distance)


#

class TestKilometer(unittest.TestCase):
    def test_init(self):
        value = 3.0
        distance = Kilometer(value)
        self.assertEqual(distance.value, value)

    def test_is_subclass_of_Distance(self):
        value = 3.0
        distance = Kilometer(value)
        self.assertIsInstance(distance, Distance)
