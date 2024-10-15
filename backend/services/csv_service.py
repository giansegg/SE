
import csv
from services.base_service import CoordsService

class CsvService(CoordsService):
    def __init__(self):
        self.csv_file = 'data/worldcities.csv'
 
    def get_coords(self, ciudad, pais):
        try:
            with open(self.csv_file, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row['city'].lower() == ciudad.lower() and row['country'].lower() == pais.lower():
                        return {'lat': float(row['lat']), 'lng': float(row['lng'])}
        except FileNotFoundError:
            print(f"El archivo {self.csv_file} no se encontró.")
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

        return None