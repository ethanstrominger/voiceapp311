from abc import ABC
from enum import Enum, auto
from math import radians, sin, cos, atan2, sqrt

from mycity.test.test_our_stuff.longlat import LongLatPoint


class Unit(Enum):
    KILOMETER = auto()
    MILE = auto()


class Distance(ABC):
    KILOMETERS_PER_MILE = 1.60934

    def __init__(self, value: float, unit: Unit):
        self.value = value
        self.unit = unit

    @classmethod
    def from_kilometers(cls, value):
        return cls(value, Unit.KILOMETER)

    @classmethod
    def from_miles(cls, value):
        return cls(value, Unit.MILE)

    @property
    def miles(self):
        if self.unit == Unit.MILE:
            return self.value
        return self.value / Distance.KILOMETERS_PER_MILE
        # if type(self) is Mile:
        #     return self.value
        # else:
        #     return self.value / Distance.KILOMETERS_PER_MILE

    @property
    def kilometers(self):
        if self.unit == Unit.KILOMETER:
            return self.value
        return self.value * Distance.KILOMETERS_PER_MILE
        # if type(self) is Kilometer:
        #     return self.value
        # else:
        #     return self.value * Distance.KILOMETERS_PER_MILE

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
        return Distance.from_kilometers(R * c)
