#!/usr/bin/env python3
import requests
import random

url = f"https://api.nobelprize.org/v1/laureate.json"

# Make API request
response = requests.get(url).json()


def intro():
    print("""\nHello, and Welcome to my Final Project!\n
My goal with this project is to provide an easy to use, well-functioning program that allows the user to search
and learn about Nobel Prizes, and Nobel Prize Laureates. Using the API from the Nobel Prize Organization itself,
I will provide the user a host of different options for digging through the vast amount of data.\n 
Enjoy!\n\n""")

def prompt():
    while True:
        prompt_choice = input("""Listed below are the different classifications you may choose from to begin your search:\n 
Enter 1 to search by Laureate Winner Name.
Enter 2 to search by Year.
Enter 3 to search by Category.
Enter q or quit to exit the program.\n
==> """)

        if prompt_choice.lower() in ('q', 'quit'):
            print("Exiting program...")
            exit()
        try:
            prompt_choice = int(prompt_choice)
        except ValueError:
            print("Please enter an integer.")
        else:
            return prompt_choice

def search_again():
    while True:
        choice = input("Would you like to search again? (y/n): ")
        if choice.lower() in ['y', 'yes']:
            return True
        elif choice.lower() in ['n', 'no']:
            print("Exiting program...")
            exit()
        else:
            print("Invalid input. Please enter 'y', 'n', 'yes', or 'no'.")


def cat_search():
    print("You have chosen to start searching by category.\n")
    while True:
        choice = input("""Let's refine how and what you want to search from the list of options below: \n
Enter 1 to display Laureates for Chemistry.
Enter 2 to display Laureates for Physics.
Enter 3 to display Laureates for Peace.
Enter 4 to display Laureates for Medicine.
Enter 5 to display Laureates for Literature.
Enter 6 to display Laureates for Economics.
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
            category = "chemistry"
        elif choice == 2:
            category = "physics"
        elif choice == 3:
            category = "peace"
        elif choice == 4:
            category = "medicine"
        elif choice == 5:
            category = "literature"
        elif choice == 6:
            category = "economics"
        else:
            print("Invalid choice. Please enter a number from 1 to 6 or q to quit.")
            continue

        print(f"Laureates for {category.capitalize()}:")
        for laureate in response["laureates"]:
            for prize in laureate["prizes"]:
                if prize["category"].lower() == category:
                    print(
                        f"{laureate.get('firstname')} {laureate.get('surname')}: Born {laureate.get('born')} in {laureate.get('bornCity')}, {laureate.get('bornCountry')}, won the Nobel {prize.get('category')} Prize in {prize.get('year')}.")
        print()
        if not search_again():
            print("Exiting program....")
            exit()

def year_search():
    print("You have chosen to start searching by Year.\n")
    while True:
        choice = input("""Let's refine how and what you want to search from the list of options below: \n
Enter 1 to search for a specific Year.
Enter 2 to search for a range of Years.
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
            year = input("Enter a year to see the Laureates for that year: ")
            year_laureates = []
            for laureate in response["laureates"]:
                for prize in laureate["prizes"]:
                    if prize["year"] == year:
                        year_laureates.append(laureate)
                        break
            if len(year_laureates) == 0:
                print(f"No Laureates were awarded in {year}.")
            else:
                print(f"Laureates for {year}:")
                for laureate in year_laureates:
                    print(
                        f"{laureate.get('firstname')} {laureate.get('surname')}: Born {laureate.get('born')} in {laureate.get('bornCity')}, {laureate.get('bornCountry')}, won the Nobel {laureate['prizes'][0]['category']} Prize.")
            print()
            if not search_again():
                print("Exiting the program...")
                exit()

        elif choice == 2:
            start_year = input("Enter the start year of the range: ")
            end_year = input("Enter the end year of the range: ")
            year_laureates = []
            for laureate in response["laureates"]:
                for prize in laureate["prizes"]:
                    if int(start_year) <= int(prize["year"]) <= int(end_year):
                        year_laureates.append(laureate)
                        break
            if len(year_laureates) == 0:
                print(f"No Laureates were awarded between {start_year} and {end_year}.")
            else:
                print(f"Laureates between {start_year} and {end_year}:")
                for laureate in year_laureates:
                    if len(laureate["prizes"]) > 0:
                        prize = laureate["prizes"][0]
                        print(
                            f"{laureate.get('firstname')} {laureate.get('surname')}: Born {laureate.get('born')} in {laureate.get('bornCity')}, {laureate.get('bornCountry')}, won the Nobel {prize.get('category')} Prize in {prize.get('year')}.")
            print()
            if not search_again():
                print("Exiting the program....")
                exit()
        else:
            print("Invalid choice. Please try again.")


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
                    print(f"{laureate.get('firstname')} {laureate.get('surname')}: Born {laureate.get('born')} in {laureate.get('bornCity')}, {laureate.get('bornCountry')}, won the Nobel {laureate['prizes'][0]['category']} Prize in {laureate['prizes'][0]['year']}.")
            print()
            if not search_again():
                print("Exiting the program....")
                exit()

        elif choice == 2:
            name = input("Enter the last name of the laureate: ")
            for laureate in response["laureates"]:
                if "surname" in laureate and name.title() in laureate["surname"]:
                    print(f"{laureate.get('firstname')} {laureate.get('surname')}: Born {laureate.get('born')} in {laureate.get('bornCity')}, {laureate.get('bornCountry')}, won the Nobel {laureate['prizes'][0]['category']} Prize in {laureate['prizes'][0]['year']}.")
            print()
            if not search_again():
                print("Exiting the program....")
                exit()

        elif choice == 3:
            print("Printing a short list of laureates...")
            laureates = random.sample(response["laureates"], 10)
            for laureate in laureates:
                print(f"{laureate.get('firstname')} {laureate.get('surname')}: Born {laureate.get('born')} in {laureate.get('bornCity')}, {laureate.get('bornCountry')}")
            print()

        else:
            print("Please enter a valid option.")
            choice = input("==> ")
