#!/usr/bin/env python3

from scratch import attributes, stats_prompt


class Player:
    def __init__(self, inventory, rooms, stats):
        self.inventory = inventory
        self.currentRoom = 'Hall'
        self.options = []
        self.stats = stats

    def showStatus(self, rooms):
        """determine the current status of the player"""
        # print the player's current location
        print('---------------------------')
        print(f"You are in the {self.currentRoom}")
        # print what the player is carrying
        print('Inventory: {self.inventory}')
        # check if there's an item in the room, if so print it
        if "item" in rooms[self.currentRoom]:
            print(f"You see a {rooms[self.currentRoom]['item']}")
        print("---------------------------")

    def pickup(self, rooms):
        if 'item' in rooms[self.currentRoom]:
            required_strength = rooms[self.currentRoom]["item"].get("weight", 0)
            required_intellect = rooms[self.currentRoom]["item"].get("smarts", 0)
            if self.stats["strength"] >= required_strength and self.stats["intellect"] >= required_intellect:
                self.inventory.append(rooms[self.currentRoom]["item"]["name"])
                del rooms[self.currentRoom]["item"]
                print("You picked up the item. ")
            else:
                print("You are not strong enough to pick up this item. ")
        else:
            print("There is nothing to pickup. ")
