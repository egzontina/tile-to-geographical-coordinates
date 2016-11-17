import math


def tile_to_geographical_coordinates(self, x, y, z):
    '''
    Function to convert tile bounds to geographical coordinates.
    Based on geographical system we have pairs:
        1. NorthWest: [lat_north, lng_west]
        2. SouthWest: [lat_end_south, lng_west]
        3. NorthEast: [lat_north, lng_end_east]
        4. SouthEast: [lat_end_south, lng_end_west]
    '''

    def tile_to_longitude(x, z):
        longitude = float(x / math.pow(2, z) * 360 - 180)
        return longitude

    def tile_to_latitude(y, z):
        n = float(math.pi - 2 * math.pi * y / math.pow(2, z))
        latitude = float(180 / math.pi * math.atan(0.5 * (math.exp(n) - math.exp(-n))))
        return latitude

    lat_north = tile_to_latitude(y, z)
    lat_end_south = tile_to_latitude(y + 1, z)
    lng_east = tile_to_longitude(x, z)
    lng_end_west = tile_to_longitude(x + 1, z)
    return json_util.dumps({ "lat": lat_north,  "lng": lng_east,  "lat_end": lat_end_south, "lng_end": lng_end_west })
