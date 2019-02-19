from mycity.test.test_our_stuff.distance import Distance
from mycity.test.test_our_stuff.longlat import LongLatPoint


class ArcGisParams(object):
    LAT_LONG_SPATIAL_REFERENCE = 4326
    MILE_UNIT = "esriSRUnit_StatuteMile"
    DEFAULT_QUERY_DISTANCE = 0.5

    def __init__(
            self,
            origin: LongLatPoint,
            distance: Distance = Distance.from_miles(DEFAULT_QUERY_DISTANCE),
            out_fields: str = "*"
    ):
        self.origin = origin
        self.url_param = {
            "f": "json",
            "inSR": self.LAT_LONG_SPATIAL_REFERENCE,
            "geometry": f"{self.origin.x},{self.origin.y}",
            "geometryType": "esriGeometryPoint",
            "returnGeometry": "false",
            "outFields": out_fields,
            "distance": distance.miles,
            "units": self.MILE_UNIT
        }

    def url_params(self):
        return self.url_param