"""
Functions for Alexa responses related to food trucks
"""

#import requests
from datetime import date
from calendar import day_name
import mycity.utilities.gis_utils as gis_utils

"""
from mycity.mycity.mycity_response_data_model import MyCityResponseDataModel
"""

FOOD_TRUCK_FEATURE_SERVER_URL = 'https://services.arcgis.com/sFnw0xNflSi8J0uh/arcgis/rest/services/' + \
                                'food_trucks_schedule/FeatureServer/0'
DAY_OF_WEEK = day_name[date.today().weekday()]

# Note: as currently written, only fetch Lunch food trucks on that day
FOOD_TRUCK_QUERY = 'Day=\'%(day)s\' AND Time=\'%(meal)s\'' % {'day': DAY_OF_WEEK, "meal": "Lunch"}

food_truck_data_result = gis_utils.get_features_from_feature_server(FOOD_TRUCK_FEATURE_SERVER_URL, FOOD_TRUCK_QUERY)

print(food_truck_data_result)