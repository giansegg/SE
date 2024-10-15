import csv
from services.base_service import CoordsService

class CsvService(CoordsService):
    def get_coords(self, ciudad, pais):
        with open(self.csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['city'].lower() == ciudad.lower() and row['country'].lower() == pais.lower():
                    return {'lat': float(row['lat']), 'lnn': float(row['lng'])}
        return None
    
