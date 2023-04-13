#!/bin/usr/env python3
"""The official Avatar Picker is here! Take the test to determine your bending abilities!"""

def yes_no_response(response):     # Takes input and returns Booleans
    """Yes no response"""
    valid_response = ["yes", "yeah", "y", "ya", "ye"]
    invalid_response = ["no", "n", "nope", "nah"]
    help_menu = ["h", "help", "?"]
    while True:
        if response.lower() in valid_response:    # using .lower() to make things easier
            return True
        if response.lower() in invalid_response:
            return False
        if response.lower() in help_menu:
            print("It doesn't get any simpler than yes or no responses!")
            response = input("Answer the question with either yes or no: ")
        else:
            print("Invalid answer. A true Bender would know to keep their answers simple! ")
            response = input("Please respond with either Yes or No: ") # prompts user
                                                                 # for a new response

# Defining the questions and passing them through my yes_no_response function
def question1():
    """Defining our first question"""
    response=input("While out in the world, do you take the time to appreciate the little things? ")
    return yes_no_response(response)

def question2():
    """Defining our second question"""
    response = input("Do you believe in the concepts of Yin and Yang, Good vs. Evil? ")
    return yes_no_response(response)

def question3():
    """Defining our third question"""
    response = input("Is it possible to attain true enlightenment? ")
    return yes_no_response(response)

def bender_score(): # I am using a counter based of the Boolean values
    """Defining Bender Score"""
    score = 0
    if question1():
        score += 1
    if question2():
        score += 1
    if question3():
        score +=1
    # creating a dictionary that pairs the "score" to the "bender_type"
    bender_types = {
            3 : "Airbender",
            2 : "Waterbender",
            1 : "Firebender",
            0 : "Earthbender"
                }
    return bender_types.get(score, "Invalid score") # This uses .get() to pull the "bender_types"
                                                    # key of our main function
