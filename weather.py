import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        # Check if city was found
        if data["cod"] != 200:
            print(f"\n❌ Error: {data['message']}")
            return

        city_name = data["name"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print(f"\n📍 City: {city_name}")
        print(f"🌡️  Temperature: {temperature}°C")
        print(f"🤔 Feels Like: {feels_like}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌤️  Condition: {description}")
        print(f"💨 Wind Speed: {wind_speed} m/s")

    except requests.exceptions.ConnectionError:
        print("\n❌ No internet connection. Please check your network.")

city = input("Enter city name: ")
get_weather(city)