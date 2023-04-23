#!/usr/bin/env python3

import requests
import random

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
Enter 4 to search by Country.
Enter q or quit to exit the program.\n
==> """)
# need to make an option to return to the main menu
        if prompt_choice.lower() in ('q', 'quit'):
            print("Exiting program...")
            exit()
        try:
            prompt_choice = int(prompt_choice)
        except ValueError:
            print("Please enter an integer.")
        else:
            return prompt_choice



def laur_name():
    print("You have chosen to start searching by name.\n")
    while True:
        choice = input("""Let's refine how and what you want to search from the list of options below: \n
Enter 1 to search by First name.
Enter 2 to search by Last name.
Enter 3 if you know a Laureate's first and last name, and would like more information about them.
Enter 4 to print a short list of Laureates.
Enter q to quit.\n
==> """)
        if choice.lower() in ('q', 'quit'):
            print("Exiting program...")
            exit()
        try:
            choice = int(choice)
        except ValueError:
            print("Please enter an integer.")
        else:
            return choice



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
        else:
            return choice


def cat_search():
    print("this")


user_choice = prompt()
if user_choice == 1:
    laur_name()
elif user_choice == 2:
    year_search()
elif user_choice == 3:
    print("success3")
elif user_choice == 4:
    print("success4")
else:
    print("Please enter a valid option.")
    user_choice = prompt()
