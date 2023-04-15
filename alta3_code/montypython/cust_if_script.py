#!/usr/bin/env python3

def main():
    weight = int(input("What is your weight in pounds?: "))
    if weight <= 100:
        print(f"At your weight of {weight} pounds you are very thin.")
    elif weight <= 200:
        print(f"At your weight of {weight} pounds you are doing ok.")
    else:
        print(f"At {weight} pounds, we need to talk about a diet...")
if __name__ == '__main__':
    main()
