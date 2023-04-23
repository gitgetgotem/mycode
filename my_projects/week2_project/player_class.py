#!/usr/bin/env python3

# Lists of responses checked later in the program
yes = ["yes", "yeah", "y", "ye", "yeehaw"]
no = ["no", "nope", "nah", "n"]

# Setting the strength and intellect scores

strength = 0
intellect = 0

# prompting the user to set their stats

print("""You have 10 points to distribute across your Character:
Strength: 
Intellect:\n""")
def stats_prompt():
    global strength, intellect
    strength = int(input("Strength: "))
    intellect = int(input("Intellect: "))

# An end game function for when the user is eaten

def end_game():
    print("You were eaten! GAME OVER")

# My attributes function, ensuring the user sets the appropriate stats, or not

def attributes():
    global strength, intellect
    stats_prompt()
    if strength + intellect == 10:
        return {"strength": strength, "intellect": intellect}
    elif strength + intellect > 10:
        print("Don't be greedy. You get 10 points to assign.")
        stats_prompt()
        return attributes()
    elif strength + intellect < 10:
        response = input("Are you sure you want to play on Hard Mode? ")
        if response in yes:
            return {"strength": strength, "intellect": intellect}
        elif response in no:
            print("Make sure you use all 10 of your allotted points!\n\n")
            stats_prompt()
            return attributes()
        else:
            print("error")
    else:
        print("error")

# Defining my Player class

class Player:
    def __init__(self, inventory, stats):
        self.inventory = inventory
        self.currentRoom = 'Hall'
        if not all(key in stats for key in ["strength", "intellect"]):
            raise ValueError("stats argument must contain strength and intellect keys")
        self.stats = stats

# The show status function that is attached to the player class, pulling from the rooms dictionary

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
        if "monster" in rooms[self.currentRoom]:
            monster_name = rooms[self.currentRoom]["monster"]["name"]
            print(f"You see a {monster_name}! ")
        print("---------------------------")

# Running checks of the player stats against the game's items to see if they can be picked up

    def pickup(self, rooms, item_name):
        if "item" in rooms[self.currentRoom]:
            for item_dict in rooms[self.currentRoom]["item"]:
                if item_dict["name"] == item_name:
                    required_strength = item_dict["required_strength"]
                    required_intellect = item_dict["required_intellect"]
                    if self.stats["strength"] >= required_strength and self.stats["intellect"] >= required_intellect:
                        self.inventory.append(item_name)
                        rooms[self.currentRoom]["item"].remove(item_dict)
                        print("You picked up the item. ")
                        break
                    else:
                        print("You don't have the ability to pick up this item! ")
                        break
            else:
                print("That item is not in the room. ")
        else:
            print("There is nothing to pickup. ")

# Checking to see if the player can slay the monster

def slay(monster_info, player):
    if all(item in player.inventory for item in monster_info["required_items"]):
        print(f"You defeated the {monster_info['name']}!")
        return True
    else:
        print(f"You need a {monster_info['required_items']} to defeat the {monster_info['name']}.")
        return False
