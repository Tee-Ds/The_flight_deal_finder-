#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
amadeus_apikey="mpeyuGDwnnnvGAECnwwfyYAnaGL7dKxX"
amadeus_secret= "SmthVYR9gCCeIhIa"
import requests
from flight_search import FlightSearch
from pprint import pprint
shetty=requests.get(url="https://api.sheety.co/a2cee85e984b97c94fa04b910d18484c/flightDeals/prices")
shetty.raise_for_status()
shetty_json=shetty.json()
sheet_data=shetty_json["prices"]
flight_search=FlightSearch()
for row in sheet_data:
    if row["iataCode"]=="":
        row["iataCode"]=flight_search.get_city_name(row["city"])
        # iata_change={
        #     "price": {
        #         "iataCode": "Testing"
        #     }
        # }
        # response= requests.put(url=f"https://api.sheety.co/a2cee85e984b97c94fa04b910d18484c/flightDeals/prices/{row["id"]}"
        #                        ,json=iata_change)





pprint(sheet_data)
