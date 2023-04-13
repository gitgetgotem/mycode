#!/bin/usr/env python3
"""The Avatar Picker!"""

from avatar_functions import bender_score

def main():
    """Called at run-time"""
    print("""So you think you have what it takes to bend the elements?
Well let's find out then, shall we? """)
    bender_type = bender_score()
    print(f"You are a(n) {bender_type}!")


if __name__ == "__main__":
    main()
