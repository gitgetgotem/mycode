#!/bin/usr/env python3
"""Slicing and dicing the trivia dictionary"""

import html


trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

trivia_escaped = {}

for key, value in trivia.items():
    if isinstance(value, str):
        trivia_escaped[key] = html.unescape(value)
    elif isinstance(value, list):
        trivia_escaped[key] = [html.unescape(answer) for answer in value]
    else:
        trivia_escaped[key] = value

def main():
    print(trivia_escaped["question"])
    user_answer = input(f"A for {trivia_escaped['incorrect_answers'][0]}\nB for {trivia_escaped['correct_answer']}\nC for {trivia_escaped['incorrect_answers'][1]}\nD for {trivia_escaped['incorrect_answers'][2]}\n=>")
    if user_answer.lower() == "b":
        print("Well done my dear")
    else:
        print("And you call yourself a movie buff....")

if __name__ == "__main__":
    main()
