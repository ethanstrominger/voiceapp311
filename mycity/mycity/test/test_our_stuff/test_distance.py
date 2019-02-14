import unittest
from abc import ABC


class Distance(ABC):
    pass


class Mile(Distance):
    def __init__(self, value: float):
        self.value = value


class Kilometer(Distance):
    def __init__(self, value: float):
        self.value = value


class TestMile(unittest.TestCase):
    def test_init(self):
        value = 3.0
        distance = Mile(value)
        self.assertEqual(distance.value, value)

    def test_is_subclass_of_Distance(self):
        value = 3.0
        distance = Mile(value)
        self.assertIsInstance(distance, Distance)


class TestKilometer(unittest.TestCase):
    def test_init(self):
        value = 3.0
        distance = Kilometer(value)
        self.assertEqual(distance.value, value)

    def test_is_subclass_of_Distance(self):
        value = 3.0
        distance = Kilometer(value)
        self.assertIsInstance(distance, Distance)
