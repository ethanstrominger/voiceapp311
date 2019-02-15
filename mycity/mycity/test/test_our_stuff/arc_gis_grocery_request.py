import requests

from mycity.test.test_our_stuff.arc_gis_params import ArcGisParams
from mycity.test.test_our_stuff.longlat import LongLatPoint


class ArcGisGroceryRequest(object):
    ARCGIS_MILE_UNIT = "esriSRUnit_StatuteMile"
    _arc_gis_url = "https://services.arcgis.com/sFnw0xNflSi8J0uh/ArcGIS/rest/services/Supermarkets_GroceryStores/FeatureServer/0/query"
    _out_fields = "Store, Address, Type, Lat, Lon, Neighborho"

    def __init__(self, origin_point: LongLatPoint):
        self._origin_point = origin_point

    def get_stripped_api_response(initial_response):
        return [element['attributes'] for element in initial_response]


    def get_nearby(self, distance):
        params = ArcGisParams (self._origin_point,distance,self._out_fields).url_param
        # params = ArcGisParams (self._origin_point,Mile(0.5),"*").url_param
        # {
        #     "f": "json",
        #     "inSR": LAT_LONG_SPATIAL_REFERENCE,
        #     "geometry": f"{self._origin_point.x},{self._origin_point.y}",
        #     "geometryType": "esriGeometryPoint",
        #     "returnGeometry": "false",
        #     "outFields": self._out_fields,
        #     "distance": distance.value,
        #     "units": self.ARCGIS_MILE_UNIT
        # }
        response = requests.get(self._arc_gis_url, params=params)
        # print (response)
        return response.json()['features']