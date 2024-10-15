from flask import Flask, request, jsonify
from services.csv_service import CsvService
from services.api_service import APIService
from services.mock_service import MockService
from flask_cors import CORS
from utils.haversine import get_distance_harvesine  



app = Flask(__name__)
CORS(app, resources={r"/data": {"origins": "http://localhost:8000"}})  

csv_service = CsvService()
api_service = APIService()
mock_service = MockService()


def get_service(option):
    if option == 'csv':
        return csv_service
    elif option == 'api':
        return api_service
    else:
        return mock_service
    
@app.route('/data', methods=['GET'])
def get_distance():
    city1 = request.args.get('city1')
    country1 = request.args.get('country1')
    city2 = request.args.get('city2')
    country2 = request.args.get('country2')
    option = request.args.get('option', 'csv')

    service = get_service(option)
    coords1 = service.get_coords(city1, country1)
    coords2 = service.get_coords(city2, country2)

    if coords1 is None or coords2 is None:
        return jsonify({'error': 'City not found'}), 404
    lat1 = float(coords1['lat'])
    lng1 = float(coords1['lng'])
    lat2 = float(coords2['lat'])
    lng2 = float(coords2['lng'])
    distance = get_distance_harvesine(lat1, lng1, lat2, lng2)  
    return jsonify({'distance': distance})


if __name__ == '__main__':
    app.run(debug=True)



    