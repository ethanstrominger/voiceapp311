from abc import ABC
import unittest
from math import radians, sin, cos, sqrt, atan2

from mycity.test.test_our_stuff.test_long_lat import LongLatPoint


class Distance(ABC):
    KILOMETERS_PER_MILE = 1.60934

    def __init__(self, value: float):
        self.value = value

    @property
    def mile(self):
        if type(self) is Mile:
            return self.value
        else:
            return self.value / Distance.KILOMETERS_PER_MILE

    @property
    def kilometer(self):
        if type(self) is Kilometer:
            return self.value
        else:
            return self.value * Distance.KILOMETERS_PER_MILE

    def get_distance(source: LongLatPoint, destination: LongLatPoint):
        """
        :param m_first: first address of interest
        :param m_second: second address of interest
        :return: the distance (in km) between these two addresses using the Haversine formula
        """
        R = 6371  # radius of the earth
        lat1 = radians(source.lat)
        lon1 = radians(source.long)
        lat2 = radians(destination.lat)
        lon2 = radians(destination.long)
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return Kilometer(R * c)


class Kilometer(Distance):
    pass


class Mile(Distance):
    pass


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
