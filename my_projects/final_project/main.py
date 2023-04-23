#!/usr/bin/env python3

import requests
import random

from project_functions import intro, prompt, laur_name, year_search, cat_search, search_again


def main():
    intro()
    user_choice = prompt()
    if user_choice == 1:
        laur_name()
    elif user_choice == 2:
        year_search()
    elif user_choice == 3:
        cat_search()
    else:
        print("Please enter a valid option.")
        user_choice = prompt()

if __name__ == "__main__":
    main()
