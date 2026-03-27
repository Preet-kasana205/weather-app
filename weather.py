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

def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "200":
            print(f"\n❌ Error: {data['message']}")
            return

        print("\n" + "=" * 40)
        print(f"  📅  5-Day Forecast for {city.title()}")
        print("=" * 40)

        # API gives forecast every 3 hours
        # We pick one reading per day (every 8th item = 24 hours)
        seen_dates = []
        for item in data["list"]:
            date = item["dt_txt"].split(" ")[0]
            
            # Only show one reading per day
            if date not in seen_dates:
                seen_dates.append(date)
                temp = item["main"]["temp"]
                description = item["weather"][0]["description"]
                emoji = get_weather_emoji(description)
                feel = get_temp_feel(temp)
                
                print(f"  {emoji} {date} | {temp}°C ({feel})")
                print(f"      condition: {description.title()}")
                print("-" * 40)

    except requests.exceptions.ConnectionError:
        print("\n❌ No internet connection.")

print("🌤️  Welcome to Weather App!")
print("=" * 40)

while True:
    print("\nWhat would you like to do?")
    print("  1️⃣  Current Weather")
    print("  2️⃣  5-Day Forecast")
    print("  3️⃣  Quit")
    print("-" * 40)
    
    choice = input("Enter choice (1/2/3): ").strip()

    if choice == "3":
        print("\n👋 Goodbye!")
        break
    elif choice not in ["1", "2"]:
        print("❌ Invalid choice! Please enter 1, 2 or 3.")
        continue

    city = input("Enter city name: ").strip()

    if city == "":
        print("❌ Please enter a city name!")
        continue

    if choice == "1":
        get_weather(city)
    elif choice == "2":
        get_forecast(city)