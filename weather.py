import requests
from dotenv import load_dotenv
import os

# Load the API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Quick check - let's make sure the key loaded correctly
print("API Key loaded:", API_KEY is not None)