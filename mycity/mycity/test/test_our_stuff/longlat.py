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