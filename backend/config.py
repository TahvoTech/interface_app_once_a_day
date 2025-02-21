import os

# Load the Cohere API key from environment variables
COHERE_API_KEY = os.getenv('COHERE_API_KEY')

if not COHERE_API_KEY:
    raise ValueError("No Cohere API key found. Please set the COHERE_API_KEY environment variable.")