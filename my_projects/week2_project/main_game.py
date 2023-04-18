"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import json

from player_class import Player, stats_prompt, attributes, slay

with open("data.json", "r") as file:
    rooms = json.load(file)

inventory = []
stats = attributes()
player = Player(inventory, stats)

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
    try:
        player.showStatus(rooms)

        move = ''
        while move == '':
            player.showStatus(rooms)
            move = input('>')

        move = move.lower().split(" ", 1)

        if move[0] == 'go':
            if move[1] in rooms[player.currentRoom]:
                player.currentRoom = rooms[player.currentRoom][move[1]]
                if 'monster' in rooms[player.currentRoom]:
                    monster_info = rooms[player.currentRoom]["monster"]
                    defeat = slay(monster_info, player)
                    if not defeat:
                        end_game()
            else:
                print('You can\'t go that way!')

        if move[0] == 'get':
            player.pickup(rooms, move[1])

        if player.currentRoom == 'Garden' and 'key' in player.inventory and 'potion' in player.inventory:
            print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
            break
    except GameOverException:
        break
