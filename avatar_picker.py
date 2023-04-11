#!/bin/usr/env python3

def yes_no_response(response):
    valid_response = ["yes", "yeah", "y", "ya", "ye"]
    invalid_response = ["no", "n", "nope", "nah"]
    while True:
        if response.lower() in valid_response:
            return True
        elif response.lower() in invalid_response:
            return False
        else:
            print("Invalid answer. A true Bender would know to keep their answers simple! ")

def question1():
    response = input("While out in the world, do you take the time to appreciate the little things? ")
    return yes_no_response(response)

def question2():
    response = input("Do you believe in the concepts of Yin and Yang, Good vs. Evil? ")
    return yes_no_response(response)

def question3():
    response = input("Is it possible to attain true enlightenment? ")
    return yes_no_response(response)

def bender_score():
    score = 0
    if question1():
        score += 1
    if question2():
        score += 1
    if question3():
        score +=1
    
    bender_types = {
            3 : "Airbender",
            2 : "Waterbender",
            1 : "Firebender",
            0 : "Earthbender"
        }
    return bender_types.get(score, "Invalid score")

def main():
    print("""So you think you have what it takes to bend the elements?
Well let's find out then, shall we? """)
    bender_type = bender_score()
    print(f"You are a {bender_type}!")
        

if __name__ == "__main__":
    main()
