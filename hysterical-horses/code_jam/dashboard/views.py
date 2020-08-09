import datetime
import os
import re
import string
import textwrap
from typing import List

import requests

import geocoder
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sessions.backends.db import SessionStore
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from geopy.geocoders import Nominatim
from pytz import timezone
from users.mixins import LevelRestrictionMixin, level_check
from .models import Search


@login_required()
def index(request):
    context = {
        "app_links": [
            {"name": name, "link": link} for name, link in request.user.app_links_gen
        ],
        "unlocked_list": [item for item in request.user.unlocked_list_gen],
        "side_stats": [
            {"name": name, "value": val}
            for name, val in request.user.side_statistics
            if val != 0
        ],
    }

    return render(request, "dashboard/index.html", context)


@login_required()
def about_view(request):
    return render(request, "dashboard/about.html", {})


def about(request):
    return render(request, "dashboard/about.html")


def search_query(search: str, format_text: bool = True):
    """ Takes in a search query and requests an API for results  """
    base_url = "https://api.duckduckgo.com/"
    payload = {"q": search, "format": "json", "pretty": "1"}
    results = requests.get(base_url, params=payload).json()
    # clipboard.copy(str(results)) # REMEMBER TO COMMENT IN AFTER DEBUGGING

    if format_text:  # formats response
        # NOTE:
        # returns as a list of entries
        # each entry is a dict with keys:
        # title (title of entry)
        # info (information about the entry/ brief description)
        # img_url (a source URL for an image relate to the entry)
        # further_info (a duckduckgo URL for more info about the entry)
        # tags (tags that relate to the entry i.e (#1, places, drinks, animals))
        def format_entry(entry: dict, tags: List):
            """ Formats a single entry  """
            pat = r">(.*)</a>(.*)"
            duckduckgo_cryptic = {"%20": " ", "%20C": ","}
            text_search = re.search(pat, entry["Result"])
            title = text_search.group(1)
            info = text_search.group(2).replace("<br>", "").replace(",", "")
            if "<a>" in title or "</a>" in title:
                url = entry["FirstURL"]
                title = url[::-1][: url[::-1].index("/")][
                    ::-1
                ]  # need to fix this up: DONE
                for k in duckduckgo_cryptic:
                    title.replace(k, duckduckgo_cryptic[k])

            # js-freindly-title makes sure the element does not have a punctuation in the id (')
            return {
                "title": title,
                "info": info,
                "img_url": entry["Icon"]["URL"],
                "further_info": entry["FirstURL"],
                "tags": tags,
            }

        formatted = []
        topics = results["RelatedTopics"]
        if results["AbstractText"] != "":
            formatted.append({"description": results["AbstractText"]})
        # parsing
        for idx, t in enumerate(topics):
            if "Name" not in t.keys():
                tags = [f"#{idx + 1}"]  # the top results
                formatted.append(format_entry(t, tags))
            else:
                tags = [t["Name"].lower()]
                for nt in t["Topics"]:
                    formatted.append(format_entry(nt, tags))
        return formatted

    else:
        return results  # else return results as is


def kelvin_to_farenheit(temp: float):
    """ Converts kelvin to farenheit  """
    far = (temp - 273.15) * (9 / 5) + 32
    return int(far)


def convert_unix_to_dt(timestamp: int, zone: str):
    """ Converts a unix to timestamp to a datetime object  """
    # first part is the date, second is time
    dt_obj = datetime.datetime.fromtimestamp(timestamp).astimezone(timezone(zone))
    return dt_obj.strftime("%m/%d %H:%M %p").split()


# queries for weather data
def weather_query(lat: str, lon: str, api_key: str, part: str, format: bool = True):
    # lon: longitude
    parts = ["minutely", "hourly", "daily"]
    parts.remove(part)
    ot_parts = ",".join(parts)
    base_url = f"https://api.openweathermap.org/data/2.5/onecall?lat=" \
               f"{lat}&lon={lon}&exclude={ot_parts}&appid={api_key}"
    res = requests.get(base_url).json()
    if format:
        # format the json
        forecast = {}
        days = []
        for d in res["daily"]:
            days.append(
                {
                    "time": convert_unix_to_dt(d["dt"], res["timezone"])[0],
                    "desc": d["weather"][0]["main"],
                    "icon": "http://openweathermap.org/img/wn/" + d["weather"][0]["icon"] + "@2x.png",
                    "min_temp": kelvin_to_farenheit(d["temp"]["min"]),
                    "max_temp": kelvin_to_farenheit(d["temp"]["max"]),
                    "avg_temp": kelvin_to_farenheit(d["temp"]["day"]),
                    "precip": int(d["pop"] * 100),
                }
            )
        forecast["daily"] = days[1:]
        forecast["current"] = {
            "date": convert_unix_to_dt(res["current"]["dt"], res["timezone"])[0],
            "time": convert_unix_to_dt(res["current"]["dt"], res["timezone"])[1],
            "main": res["current"]["weather"][0]["main"],
            "desc": string.capwords(res["current"]["weather"][0]["description"]),
            "icon": "http://openweathermap.org/img/wn/" + res["current"]["weather"][0]["icon"] + "@2x.png",
            "current_temp": kelvin_to_farenheit(res["current"]["temp"]),
            "feels_like": kelvin_to_farenheit(res["current"]["feels_like"]),
            "humidity": res["current"]["humidity"],
            "wind_speed": res["current"]["wind_speed"],
            "sunrise": convert_unix_to_dt(res["current"]["sunrise"], res["timezone"])[
                1
            ],
            "sunset": convert_unix_to_dt(res["current"]["sunset"], res["timezone"])[1],
        }
        forecast["tz"] = res["timezone"]
        return forecast
    else:
        return res  # return as is


@login_required()
def weather_results(request, ip_address: str):
    api_key = os.environ.get("weather_api_key")
    pat = re.compile(
        r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    )
    error_msg = ""
    if re.search(pat, ip_address):
        user_data = geocoder.ip(
            ip_address
        ).latlng  # change to visitor_ip_address in developement
        latitude, longitude = (
            user_data[0],
            user_data[1],
        )  # easily get lat. and lon. of location
    else:
        geolocator = Nominatim(user_agent="hyst_horses")
        location = geolocator.geocode(ip_address)
        latitude, longitude = getattr(location, "latitude", None), getattr(location, "longitude", None)
        if latitude and longitude:
            wrapper = textwrap.TextWrapper(width=20)
            shortened = wrapper.wrap(text=ip_address)[0]
            if shortened != ip_address:
                shortened += "..."
            error_msg = f"No weather found for {shortened}."
            latitude, longitude = "", ""
    if latitude and longitude:
        forecast = weather_query(latitude, longitude, api_key, "daily")
        current_time = datetime.datetime.now(timezone(forecast["tz"])).strftime(
            "%H:%M %p"
        )
    else:
        forecast = {"daily": "", "current": ""}
        current_time = ""
    context = {
        "day_forecast": forecast["daily"],
        "current_details": forecast["current"],
        "ending": "°F",
        "current_time": current_time,
        "error_msg": error_msg,
    }
    loc_address = getattr(location, "address")
    if not loc_address:
        loc_address = ""
    context["address"] = loc_address
    return render(request, "dashboard/weather/weather.html", context=context)


class WeatherView(LoginRequiredMixin, LevelRestrictionMixin, View):
    def test_func(self):
        return self.request.user.weather_unlocked

    def get(self, request, **kwargs):
        ip_address = kwargs["ip_address"]
        api_key = os.environ.get("weather_api_key")
        pat = re.compile(
            r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        )
        error_msg = ""

        if re.search(pat, ip_address):
            # Change to visitor_ip_address in developement
            user_data = geocoder.ip(ip_address).latlng

            # Easily get lat. and lon. of location
            latitude, longitude = user_data[0], user_data[1]
        else:
            geolocator = Nominatim(user_agent="hyst_horses")
            location = geolocator.geocode(ip_address)
            latitude, longitude = getattr(location, "latitude", None), getattr(location, "longitude", None)
            if not(latitude and longitude):
                wrapper = textwrap.TextWrapper(width=20)
                shortened = wrapper.wrap(text=ip_address)[0]
                if shortened != ip_address:
                    shortened += "..."
                error_msg = f"No weather found for {shortened}."
                latitude, longitude = "", ""

        if latitude and longitude:
            forecast = weather_query(latitude, longitude, api_key, "daily")
            current_time = datetime.datetime.now(timezone(forecast["tz"])).strftime(
                "%H:%M %p"
            )
        else:
            forecast = {"daily": "", "current": ""}
            current_time = ""

        context = {
            "day_forecast": forecast["daily"],
            "current_details": forecast["current"],
            "ending": "°F",
            "current_time": current_time,
            "error_msg": error_msg,
        }
        return render(request, "dashboard/weather/weather.html", context)

    def post(self, request, *args, **kwargs):
        # Most of it actually done via javascript in the html file
        return HttpResponseRedirect(self.request.path_info)


# needs to be global otherwise session gets
# reinstantiated each time
global hist_store
hist_store = SessionStore()


@login_required()
def engine_results(request, search_text: str):
    """ Renders a page for the request  """
    # queries that have some problems:
    # prevent long searches from overflowing
    wrapper = textwrap.TextWrapper(width=12)
    shortened = wrapper.wrap(text=search_text)[0]
    if shortened != search_text:
        shortened += "..."

    # session info for history

    try:
        old_val = hist_store["history"]
        hist_store["history"] = old_val + [(shortened, search_text)]
    except KeyError:
        hist_store["history"] = [(shortened, search_text)]
    hist = hist_store["history"][-3:]

    res = search_query(search_text)

    if search_text not in Search.objects.filter(
        author=request.user, content=search_text
    ):
        this_search = Search.objects.create(author=request.user, content=search_text)
        this_search.save()

    top_results = []
    other_results = []
    desc = ""
    for r in res:
        if "tags" in r.keys():
            if r["tags"][0] in ["#1", "#2", "#3"]:
                top_results.append(r)
            else:
                other_results.append(r)
        elif "description" in r.keys():
            desc = r["description"]

    context = {
        "search": search_text,
        "top_results": top_results,
        "other_results": other_results,
        "description": desc,
        "version_number": "1.1",
        "entries_length": len(top_results + other_results),
        "past_history": hist,
    }

    return render(request, "dashboard/search-engine/results.html", context=context)


@login_required()
@user_passes_test(
    lambda user: level_check(user, unlock=8),
    login_url="dashboard-index",
    redirect_field_name=None,
)
def chat_room(request, room_name):
    context = {"room_name": room_name}
    return render(request, "dashboard/chat_room.html", context)


# things to do:
# if not enough info is given for a single entry call the entry as a query and send results (for example: )
# llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch
