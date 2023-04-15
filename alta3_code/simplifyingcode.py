#!/bin/usr/env python3
"""Figuring out your Zodiac Sign!"""
usr_name = input("What is your name? ").title()
year = int(input("What year were you born? --> "))
zodiac_year = year % 12

sign = {
        4 : ["Rabbit", "vigilant, witty, quick-minded, and ingenious."],
        5 : ["Rat", "artistic, sociable, industrious, charming, and intelligent."],
        6 : ["Tiger", "courageous, enthusiastic, confident, charismatic, and a leader."],
        7 : ["Ox", "strong, thorough, determined, loyal, and reliable."],
        8 : ["Dragon", "talented, powerful, lucky, and successfull."],
        9 : ["Snake", "wise, like to work alone, and determined."],
        10 : ["Horse", "animated, active, and energetic."],
        11 : ["Sheep", "creative, resilient, gentle, mild-mannered, and shy."],
        0 : ["Monkey", "sharp, smart, curious, and mischievious."],
        1 : ["Rooster", "hardworking, resourceful, courageous, and talented."],
        2 : ["Dog", "loyal, honest, cautious, and kind."],
        3 : ["Pig", "a symbol of wealth, honesty, and practicality."]
        }

print(f"{usr_name} your zodiac sign is {sign[zodiac_year][0]}, you are {sign[zodiac_year][1]}")
