#!/usr/bin/python3
import requests

from pprint import pprint

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

year = int(input("Pick a year: "))
day = int(input("Pick a date: "))
month = int(input("Pick a month (1-12)"))

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## update the date below, if you like
    startdate = f"start_date={year}-{month}-{day}"

    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    pprint(neodata)

if __name__ == "__main__":
    main()

