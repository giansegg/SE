import requests
from services.base_service import CoordsService

class APIService(CoordsService):
    def get_coords(self, ciudad, pais):
        url = f"https://nominatim.openstreetmap.org/search?q={ciudad},{pais}&format=json"
        response = requests.get(url)
        if response.status_code == 200 and response.json():
            data = response.json()[0]
            return {'lat': float(data['lat']), 'lon': float(data['lng'])}
        return None