"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import json

# importing my functions

from player_class import Player, stats_prompt, attributes, slay, end_game

with open("data.json", "r") as file:
    rooms = json.load(file)

# setting up my player class, inventory, stats etc.

inventory = []
stats = attributes()
player = Player(inventory, stats)

# the instructions for the game

def showInstructions():
    """Show the game instructions when called"""
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')

# What all help menu's should look like

def help_menu():
    print('Available commands: go, get, help')

showInstructions()

# Main function

def main():
    while True:
        try:
            move = ''
            while move == '':
                player.showStatus(rooms)
                move = input('>')

            move = move.lower().split(" ", 1)

            if move[0] in ["h", "help"]:
                help_menu()
                continue

            if move[0] == 'go':
                if move[1] in rooms[player.currentRoom]:
                    player.currentRoom = rooms[player.currentRoom][move[1]]
                    if 'monster' in rooms[player.currentRoom]:
                        monster_info = rooms[player.currentRoom]["monster"]
                        print(f"You see a {monster_info['name']}!")
                        defeat = slay(monster_info, player)
                        if defeat:
                            del(rooms[player.currentRoom]["monster"])
                        if not defeat:
                            end_game()
                            break
                else:
                    print('You can\'t go that way!')

            if move[0] == 'get':
                player.pickup(rooms, move[1])

            if player.currentRoom == 'Garden' and 'key' in player.inventory and 'potion' in player.inventory:
                print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
                break
        except GameOverException:
            break

if __name__ == "__main__":
    main()
