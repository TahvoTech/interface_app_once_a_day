import os
from flask import Blueprint, jsonify
import cohere

main_routes = Blueprint('main_routes', __name__)

# Access the Cohere API key from environment variables
cohere_api_key = os.getenv('COHERE_API_KEY')
cohere_client = cohere.Client(cohere_api_key)

@main_routes.route('/')
def home():
    return jsonify({"message": "Hello, Interface App Once a Day!"})