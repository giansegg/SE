import math 


def get_distance_harvesine(lat1, lng1, lat2, lng2):
    r= 6371
    dif_lat = math.radians(lat2 - lat1)
    dif_lon = math.radians(lng2 - lng1)
    a = math.sin(dif_lat/2) * math.sin(dif_lat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dif_lon/2) * math.sin(dif_lon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = r * c
    return distance

    