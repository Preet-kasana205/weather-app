import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
def get_weather_emoji(description):
    description = description.lower()
    if "thunder" in description:
        return "⛈️"
    elif "rain" in description or "drizzle" in description:
        return "🌧️"
    elif "snow" in description:
        return "❄️"
    elif "cloud" in description:
        return "☁️"
    elif "clear" in description:
        return "☀️"
    elif "haze" in description or "mist" in description or "fog" in description:
        return "🌫️"
    else:
        return "🌤️"

def get_temp_feel(temp):
    if temp >= 35:
        return "🔥 Very Hot"
    elif temp >= 25:
        return "😊 Warm"
    elif temp >= 15:
        return "🙂 Mild"
    elif temp >= 5:
        return "🧥 Cold"
    else:
        return "🥶 Very Cold"

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

        emoji = get_weather_emoji(description)
        temp_feel = get_temp_feel(temperature)

        print("\n" + "=" * 40)
        print(f"  {emoji}  Weather in {city_name}")
        print("=" * 40)
        print(f"  🌡️  Temperature : {temperature}°C  ({temp_feel})")
        print(f"  🤔 Feels Like  : {feels_like}°C")
        print(f"  💧 Humidity    : {humidity}%")
        print(f"  🌤️  Condition   : {description.title()}")
        print(f"  💨 Wind Speed  : {wind_speed} m/s")
        print("=" * 40)

    except requests.exceptions.ConnectionError:
        print("\n❌ No internet connection. Please check your network.")

print("🌤️  Welcome to Weather App!")
print("Type a city name to get weather or 'quit' to exit\n")

while True:
    city = input("Enter city name: ")
    
    if city.lower() == "quit":
        print("\n👋 Goodbye!")
        break
    
    if city.strip() == "":
        print("❌ Please enter a city name!")
        continue
    
    get_weather(city)
    print()