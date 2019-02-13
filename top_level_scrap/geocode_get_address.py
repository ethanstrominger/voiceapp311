import os
os.environ['GOOGLE_MAPS_API_KEY'] = "Test"
from mycity.utilities.gis_utils import geocode_address
address = "399 Boylston St"
result = geocode_address(address)
print(result)
