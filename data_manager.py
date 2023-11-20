import requests
from pprint import pprint
from os import environ

SHEETY_ENDPOINT = environ["SHEETY_ENDPOINT"]


class DataManager:
    # # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination = {}

    def get_destination(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination = data["prices"]
        return self.destination

    def update_destination_code(self):
        for city in self.destination:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

