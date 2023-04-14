#!/usr/bin/env python3

import requests

from pprint import pprint

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi['sprites']['front_default'])
    for move in pokeapi['moves']:
        print(move['move']['name'])
    pprint(pokeapi['game_indices'])
    count = 0
    game_count = len(pokeapi['game_indices'])
    print(game_count)

main()

