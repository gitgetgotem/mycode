#!/bin/usr/env python3
"""The official Avatar Picker is here! Take the test to determine your bending abilities!"""

def yes_no_response(response):     # This function takes the users response, checks it against the given lists,
    valid_response = ["yes", "yeah", "y", "ya", "ye"]  # and returns a Boolean Value
    invalid_response = ["no", "n", "nope", "nah"]
    help_menu = ["h", "help", "?"]
    while True:
        if response.lower() in valid_response:    # using .lower() to make things easier
            return True
        elif response.lower() in invalid_response:
            return False
        elif response.lower() in help_menu:
            print("It doesn't get any simpler than yes or no responses!")
            response = input("Answer the question with either yes or no: ")
        else:
            print("Invalid answer. A true Bender would know to keep their answers simple! ")
            response = input("Please respond with either Yes or No: ") # In the case of an invalid response, prompts
# the user for a new response


# This is where I am defining the questions and passing them through my yes_no_response function
def question1():
    response = input("While out in the world, do you take the time to appreciate the little things? ")
    return yes_no_response(response)

def question2():
    response = input("Do you believe in the concepts of Yin and Yang, Good vs. Evil? ")
    return yes_no_response(response)

def question3():
    response = input("Is it possible to attain true enlightenment? ")
    return yes_no_response(response)

def bender_score(): # I am using a counter based of the Boolean values of the responses to the queastions
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
    return bender_types.get(score, "Invalid score") # This uses .get() to pull the associated value for the "bender_types" key
# our main function


def main():
    print("""So you think you have what it takes to bend the elements?
Well let's find out then, shall we? """)
    bender_type = bender_score()
    print(f"You are a(n) {bender_type}!")
        

if __name__ == "__main__":
    main()
