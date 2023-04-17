#!/usr/bin/env python3

from scratch import attributes, stats_prompt


class Player:
    def __init__(self, inventory, rooms, stats=None):
        self.inventory = inventory
        self.currentRoom = 'Hall'
        self.stats = stats or {"strength": 0, "speed": 0, "intellect": 0}
        print(self.stats)

    def showStatus(self, rooms):
        """determine the current status of the player"""
        # print the player's current location
        print('---------------------------')
        print(f"You are in the {self.currentRoom}")
        # print what the player is carrying
        print(f'Inventory: {self.inventory}')
        # check if there's an item in the room, if so print it
        if "item" in rooms[self.currentRoom]:
            item_names = [item["name"] for item in rooms[self.currentRoom]["item"]]
            print(f"You see a {', '.join(item_names)}")
        print("---------------------------")

    def pickup(self, rooms, item_name):
        print(rooms)
        if "item" in rooms[self.currentRoom]:
            for item_dict in rooms[self.currentRoom]["item"]:
                if item_dict["name"] == item_name:
                    required_strength = item_dict.get("weight", 0)
                    required_intellect = item_dict.get("smarts", 0)
                    if self.stats.get("strength", 0) >= required_strength and self.stats.get("intellect", 0) >= required_intellect:
                        self.inventory.append(item_name)
                        rooms[self.currentRoom]["item"].remove(item_dict)
                        print("You picked up the item. ")
            else:
                print("You are not strong enough to pick up this item. ")
        else:
            print("There is nothing to pickup. ")
