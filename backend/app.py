from flask import Flask, request, jsonify
from services.csv_service import CsvService
from services.api_service import APIService
from services.mock_service import MockService


app = Flask(__name__)


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
    coords1 = service.get_distance(city1, country1)
    coords2 = service.get_distance(city2, country2)

    if coords1 is None or coords2 is None:
        return jsonify({'error': 'City not found'}), 404
    else:
        return jsonify({'distance': service.calculate_distance(coords1, coords2)})


if __name__ == '__main__':
    app.run(debug=True)



    