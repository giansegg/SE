import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from app import app  

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

if __name__ == '__main__':
    unittest.main()
