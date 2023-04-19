from pprint import pprint
import requests
import json
import http

# https://www.nobelprize.org/about/developer-zone-2/

#API = "https://api.nobelprize.org/2.1/laureates"

#resp = requests.get(f"{API}")


url = "http://api.nobelprize.org/v1/country.json"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

pprint(response.text)
