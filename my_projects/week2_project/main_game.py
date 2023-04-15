"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import json

from player_class import Player

with open("data.json", "r") as file:
    rooms = json.load(file)

player = Player([], rooms)

def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')


showInstructions()

# breaking this while loop means the game is over
while True:
    player.showStatus(rooms)

    # the player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[player.currentRoom]:
            # set the current room to the new room
            player.currentRoom = rooms[player.currentRoom][move[1]]
        # if they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[player.currentRoom] and move[1] in rooms[player.currentRoom]['item']:
            # add the item to their inventory
            player.inventory.append(move[1])
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item key:value pair from the room's dictionary
            del rooms[player.currentRoom]['item']
        # if there's no item in the room or the item doesn't match
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
        ## If a player enters a room with a monster

    if 'item' in rooms[player.currentRoom] and 'monster' in rooms[player.currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in player.inventory and 'potion' in player.inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break
