#!/bin/usr/env python3
"""Simpsons slicing challenge"""

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]


def challenge_list():
    print(f"My {challenge[2][1]}! The {challenge[2][0]} do {challenge[3]}!")

def trial_list():
    print(f"My {trial[2]['goggles']}! The {trial[2]['eyes']} do {trial[3]}!")

def nightmare_list():
    print(f"My {nightmare[0]['user']['name']['first']}! The {nightmare[0]['kumquat']} do {nightmare[0]['d']}!")

def main():
    challenge_list()
    trial_list()
    nightmare_list()

if __name__ == "__main__":
    main()
