import requests
from datetime import datetime


def get_weather(lat: float, lon: float) -> dict:
    """
    Take latitude and longitude to get weather data
    using openweather api and return data in dict format
    """
    weather_key = '0a2c03e9dee2533389d7b459d0f8595e'
    # source contain JSON data from API
    source = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_key}')
    # list_of_data contain json encoded content
    list_of_data = source.json()
    data = {"weather": {
        "celsius": int(list_of_data['main']['temp'])-272,
        "fahrenheit": int(((list_of_data['main']['temp'])-272)*1.8+32)},
        "city": str(list_of_data['name']),
        "sunset": datetime.fromtimestamp(
            list_of_data['sys']['sunset']),
        "sunrise": datetime.fromtimestamp(
            list_of_data['sys']['sunset']),
        }
    return data


if __name__ == "__main__":
    weather_data = get_weather(21.178, 72.83)
