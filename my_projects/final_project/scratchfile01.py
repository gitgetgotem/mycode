#give list of winners, have users input which they would like to know more about
from pprint import pprint
import requests
import http

# https://www.nobelprize.org/about/developer-zone-2/

#API = "https://api.nobelprize.org/2.1/laureates"

#resp = requests.get(f"{API}")


url = "https://api.nobelprize.org/2.1/nobelPrizes"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers).json()

pprint(response["nobelPrizes"][0])
