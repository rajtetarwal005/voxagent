import requests
from langchain.tools import tool
from app.config import settings


@tool
def get_weather(city: str) -> str:
    """Get current weather of a city"""

    try:
        url = "http://api.weatherapi.com/v1/current.json"

        params = {
            "key": settings.WEATHER_API_KEY,
            "q": city,
            "aqi": "no"
        }

        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if "error" in data:
            return f"Weather API Error: {data['error']['message']}"

        location = data["location"]["name"]
        region = data["location"]["region"]
        country = data["location"]["country"]

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        return f"{location}, {region}, {country}: {temp}°C, {condition}"

    except Exception as e:
        return f"Error fetching weather: {str(e)}"


if __name__ == "__main__":
    print(get_weather.invoke("motisar, jhunjhunu, rajasthan"))