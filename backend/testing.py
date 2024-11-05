import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from app import app  
from services.api_service import APIService
from services.mock_service import MockService


class TestDistanceAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.csv_service')
    def test_city_not_found(self, mock_csv_service):

        mock_csv_service.get_coords.side_effect = lambda city, country: None if city == "NOEXISTE" else {'lat': 33.3333, 'lng': 222.222}
        response = self.app.get('/data?city1=NOEXISTE&country1=FantasyLand&city2=New%20York&country2=USA&option=csv')
        
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json, {'error': 'City not found'})

    @patch('app.csv_service')
    def test_same_city_distance(self, mock_csv_service):

        mock_csv_service.get_coords.return_value = {'lat': 33.3333, 'lng': 222.222} 
        response = self.app.get('/data?city1=New%20York&country1=USA&city2=New%20York&country2=USA&option=csv')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['distance'], 0)




class TestAPIService(unittest.TestCase):

    def setUp(self):

        self.api_service = APIService()

    def test_get_coords_valid_city(self):

        coords = self.api_service.get_coords("Tokyo", "Japan")

        self.assertIsNotNone(coords)
        self.assertIn("lat", coords)
        self.assertIn("lng", coords)
        print(f"Coordenadas para Tokyo: {coords}")  

    def test_get_coords_invalid_city(self):

        coords = self.api_service.get_coords("INEXISTENTE", "NOEXISTE")

        self.assertIsNone(coords)
        print("Coordenadas para INEXISTENTE: None")  



class TestMockService(unittest.TestCase):
    def setUp(self):
        self.mock_service = MockService()

    def test_get_coords_always_zero(self):
        coords = self.mock_service.get_coords("Cualquier", "Cualquier")
        self.assertEqual(coords, {"lat": 0, "lng": 0})
        print("MockService siempre devuelve: {'lat': 0, 'lng': 0}")  



if __name__ == '__main__':
    unittest.main()
