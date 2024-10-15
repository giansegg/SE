from flask import Flask, request, jsonify
from services.csv_service import CsvService
from services.api_service import ApiService
from services.mock_service import MockService




app = Flask(__name__)


csv_service = CsvService()
api_service = ApiService()
mock_service = MockService()


def get_service()