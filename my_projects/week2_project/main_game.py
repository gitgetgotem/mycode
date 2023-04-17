"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import json

from player_class import Player
from scratch import stats_prompt, attributes

with open("data.json", "r") as file:
    rooms = json.load(file)

inventory = []
stats = dict(zip(["strength", "speed", "intellect"], attributes()))

player = Player(inventory, stats=stats)

def showInstructions():
    """Show the game instructions when called"""
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')


showInstructions()

while True:
    player.showStatus(rooms)

    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split(" ", 1)

    if move[0] == 'go':
        if move[1] in rooms[player.currentRoom]:
            player.currentRoom = rooms[player.currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

    if move[0] == 'get':
        player.pickup(rooms, move[1])

    if 'item' in rooms[player.currentRoom] and 'monster' in rooms[player.currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    if player.currentRoom == 'Garden' and 'key' in player.inventory and 'potion' in player.inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
