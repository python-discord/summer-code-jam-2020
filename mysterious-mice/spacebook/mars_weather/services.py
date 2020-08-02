import requests

MARS_URL = (
    "https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"
)


def get_current_weather(request):
    """
    If user reloads the page, used cached data instead of making call to API again.
    """
    is_cached = "weather_data" in request.session

    if not is_cached:
        print("No data cached.")
        response = requests.get(MARS_URL)
        request.session["weather_data"] = response.json()

    weather_data = request.session["weather_data"]

    current_sol = weather_data["sol_keys"][-1]

    return {
        "atmospheric_temperature": weather_data[current_sol]["AT"]["av"],
        "atmospheric_pressure": weather_data[current_sol]["PRE"]["av"],
        "horizontal_wind_speed": weather_data[current_sol]["HWS"]["av"],
    }


def get_week_weather(request):
    """
    If user reloads the page, used cached data instead of making call to API again.
    """
    is_cached = "weather_data" in request.session

    if not is_cached:
        print("No data cached.")
        response = requests.get(MARS_URL)
        request.session["weather_data"] = response.json()

    weather_data = request.session["weather_data"]

    return {
        "day_one": weather_data[weather_data["sol_keys"][0]],
        "day_two": weather_data[weather_data["sol_keys"][1]],
        "day_three": weather_data[weather_data["sol_keys"][2]],
        "day_four": weather_data[weather_data["sol_keys"][3]],
        "day_five": weather_data[weather_data["sol_keys"][4]],
        "day_six": weather_data[weather_data["sol_keys"][5]],
        "day_seven": weather_data[weather_data["sol_keys"][6]],
    }
