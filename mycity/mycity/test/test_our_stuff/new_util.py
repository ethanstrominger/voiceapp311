from typing import List

from mycity.test.test_our_stuff.distance import Distance
from mycity.test.test_our_stuff.longlat import LongLatPoint


def add_distances_to_api_response(origin, grocery_store_api_response:List):
    # print("A===")
    # print(grocery_store_api_response)
    for store_json in grocery_store_api_response:
        # print("B===")
        # print(store_json)
        # destination = LongLatPoint(store_json2.lon,store_json2.lat)
        destination = LongLatPoint(store_json["Lon"],store_json["Lat"])
        store_json['distance_in_miles'] = Distance.get_distance(origin,destination).mile