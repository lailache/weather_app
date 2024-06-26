import requests
import json

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises a HTTPError if the response was an HTTP error status.
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return None

    weather_data = response.json()

    # Check if the city was found
    if weather_data["cod"] == "404":
        print("The city was not found.")
        return None

    return weather_data

def display_weather(weather_data):
    if weather_data is None:
        return

    city = weather_data["name"]
    description = weather_data["weather"][0]["description"]
    temp = weather_data["main"]["temp"]

    print(f"Weather in {city}:")
    print(f"{description.capitalize()}")
    print(f"Temperature: {temp}°C")

def main():
    api_key = "your_api_key_here"
    city = "Yerevan"

    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
