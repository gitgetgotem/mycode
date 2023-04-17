#!/usr/bin/env python3

# give user a set number of "points" to assign to three different attributes,
# as strength, speed, and intellect, and then have conditions based off of that.
# i.e. you need certain strength to pick up certain items, certain speed to runaway,
# and certain intellect to maybe figure out a problem or find a trap door.

yes = ["yes", "yeah", "y", "ye", "yeehaw"]
no = ["no", "nope", "nah", "n"]

strength = 0
speed = 0
intellect = 0

print("""You have 10 points to distribute across your Character:
Strength: 
Speed:
Intellect:\n""")
def stats_prompt():
    global strength, speed, intellect
    strength = int(input("Strength: "))
    speed = int(input("Speed: "))
    intellect = int(input("Intellect: "))


def attributes():
    global strength, speed, intellect
    stats_prompt()
    if strength + speed + intellect == 10:
        return {strength, speed, intellect}
    elif strength + speed + intellect > 10:
        print("Don't be greedy. You get 10 points to assign.")
        stats_prompt()
        return attributes()
    elif strength + speed + intellect < 10:
        response = input("Are you sure you want to play on Hard Mode? ")
        if response in yes:
            return {strength, speed, intellect}
        elif response in no:
            print("Make sure you use all 10 of your allotted points!\n\n")
            stats_prompt()
            return attributes
        else:
            print("working on it")
    else:
        print("working on it")


