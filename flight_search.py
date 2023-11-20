from os import environ
import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = environ["API_KEY"]

class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {
            "apikey": API_KEY,
        }
        query = {
            "term": city_name
        }
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        response.raise_for_status()
        code = response.json()["locations"][0]["code"]
        return code
