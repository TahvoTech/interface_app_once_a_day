import os
from flask import Flask
from flask_cors import CORS
from routes import main_routes
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(main_routes)

if __name__ == '__main__':
    app.run(debug=True)