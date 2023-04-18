#!/usr/bin/env python3

yes = ["yes", "yeah", "y", "ye", "yeehaw"]
no = ["no", "nope", "nah", "n"]

strength = 0
intellect = 0

print("""You have 10 points to distribute across your Character:
Strength: 
Intellect:\n""")
def stats_prompt():
    global strength, intellect
    strength = int(input("Strength: "))
    intellect = int(input("Intellect: "))


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
            print("working on it")
    else:
        print("working on it")


class Player:
    def __init__(self, inventory, stats):
        self.inventory = inventory
        self.currentRoom = 'Hall'
        if not all(key in stats for key in ["strength", "intellect"]):
            raise ValueError("stats argument must contain strength and intellect keys")
        self.stats = stats


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
                        print("You are not strong enough to pick up this item. ")
                        break
            else:
                print("That item is not in the room. ")
        else:
            print("There is nothing to pickup. ")


    def fight(self, monster):
        """Determine if the player can win"""
        if monster.item_required in self.inventory:
            print(f"You defeated the {monster.name} with the {monster.item_required}! ")
            return True
        else:
            print


class Monster:
    def __init__(self, name, required_item):
        self.name = name
        self.required_item = required_item

    def defeat(self, player):
        if self.required_item in player.inventory:
            print(f"You defeated the {self.name}!")
        else:
            print(f"You need a {self.required_item} to defeat the {self.name}.")
