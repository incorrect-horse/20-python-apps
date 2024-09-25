# https://openweathermap.org/api

import requests
import os

API_KEY = os.getenv("API_KEY_WX_FORECAST_APP")

def get_data(place, days=1):
    url = "https://api.openweathermap.org/data/2.5/forecast?"\
          f"q={place}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    forecast_days = 8 * days
    filtered_data = filtered_data[:forecast_days]
    return filtered_data


if __name__ == "__main__":
    get_data(place="Tokyo", days=3)
