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
        response = requests.get(MARS_URL)
        request.session["weather_data"] = response.json()

    weather_data = request.session["weather_data"]

    current_sol = weather_data["sol_keys"][-1]

    context = dict.fromkeys(["AT", "PRE", "HWS"])

    for measurement in context.keys():
        if weather_data["validity_checks"][current_sol][measurement]["valid"]:
            context[measurement] = weather_data[current_sol][measurement]

    context["season"] = weather_data[current_sol]["Season"]

    return context


def get_week_weather(request):
    """
    If user reloads the page, used cached data instead of making call to API again.
    """
    is_cached = "weather_data" in request.session

    if not is_cached:
        response = requests.get(MARS_URL)
        request.session["weather_data"] = response.json()

    weather_data = request.session["weather_data"]

    return {
        "weekly_weather": [
            {weather_data["sol_keys"][0]: weather_data[weather_data["sol_keys"][0]]},
            {weather_data["sol_keys"][1]: weather_data[weather_data["sol_keys"][1]]},
            {weather_data["sol_keys"][2]: weather_data[weather_data["sol_keys"][2]]},
            {weather_data["sol_keys"][3]: weather_data[weather_data["sol_keys"][3]]},
            {weather_data["sol_keys"][4]: weather_data[weather_data["sol_keys"][4]]},
            {weather_data["sol_keys"][5]: weather_data[weather_data["sol_keys"][5]]},
            {weather_data["sol_keys"][6]: weather_data[weather_data["sol_keys"][6]]},
        ],
    }
