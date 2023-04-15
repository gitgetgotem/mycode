#!/bin/usr/env python3
"""Looping with for Challenge"""

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

def main():
    which_farm = input("""Choose which farm you would like information on:
A. NE Farm
B. W Farm
C. SE Farm
=>""").lower()
    for farm in farms:
        if which_farm == "a":
            print(farms[0]['agriculture'])
            break
        elif which_farm == "b":
            print(farms[1]['agriculture'])
            break
        elif which_farm == "c":
            print(farms[2]['agriculture'])
            break
        else:
            print("Invalid response.")

if __name__ == "__main__":
    main()
