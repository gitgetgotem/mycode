import requests
import random

url = f"https://api.nobelprize.org/v1/laureate.json"

# Make API request
response = requests.get(url).json()


def laur_name():
    print("You have chosen to start searching by name.\n")
    while True:
        choice = input("""Let's refine how and what you want to search from the list of options below: \n
Enter 1 to search by First name.
Enter 2 to search by Last name.
Enter 3 to print a short list of Laureates.
Enter q to quit.\n
==> """)
        if choice.lower() in ('q', 'quit'):
            print("Exiting program...")
            exit()
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter an integer.")
            continue
        if choice == 1:
            name = input("Enter the first name of the laureate: ")
            for laureate in response["laureates"]:
                if "firstname" in laureate and name.title() in laureate["firstname"]:
                    print(f"{laureate['firstname']} {laureate['surname']}: Born {laureate['born']} in {laureate['bornCity']}, {laureate['bornCountry']}, won the Nobel {laureate['prizes'][0]['category']} Prize in {laureate['prizes'][0]['year']}.")
            print()

        elif choice == 2:
            name = input("Enter the last name of the laureate: ")
            for laureate in response["laureates"]:
                if "surname" in laureate and name.title() in laureate["surname"]:
                    print(f"{laureate['firstname']} {laureate['surname']}: Born {laureate['born']} in {laureate['bornCity']}, {laureate['bornCountry']}, won the Nobel {laureate['prizes'][0]['category']} Prize in {laureate['prizes'][0]['year']}.")
            print()

        elif choice == 3:
            print("Printing a short list of laureates...")
            laureates = random.sample(response["laureates"], 10)
            for laureate in laureates:
                print(f"{laureate['firstname']} {laureate['surname']}: Born {laureate['born']} in {laureate['bornCity']}, {laureate['bornCountry']}")
            print()

        else:
            print("Please enter a valid option.")
            choice = input("==> ")


