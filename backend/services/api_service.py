import requests
from services.base_service import CoordsService



class APIService:
    def get_coords(self, city, country):
        headers = {
            'User-Agent': 'YourAppName/1.0 (your_email@example.com)'  # Reemplaza con tu información
        }
        print(f"Requesting coordinates for: {city}, {country}")
        try:
            response = requests.get(f'https://nominatim.openstreetmap.org/search?q={city},{country}&format=json', headers=headers)
            if response.status_code == 200:
                data = response.json()
                if data:
                    print(f"Coordinates found: {data[0]['lat']}, {data[0]['lon']}")
                    return {'lat': data[0]['lat'], 'lng': data[0]['lon']}
                else:
                    print(f"No coordinates found for {city}, {country}")
            else:
                print(f"API error: {response.status_code}")
        except Exception as e:
            print(f"Exception occurred: {e}")
        return None