#!/bin/usr/env python3
"""Let's get spooky!"""


def main():
    with open("dracula.txt", "r") as dracula_obj:
        with open("vampytimex.txt", "w") as vamps:
            count = 0
            for line in dracula_obj:
                if "vampire" in line.lower():
                    count += 1
                    print(line)
                    vamps.write(line)
        print(count)


if __name__ == "__main__":
    main()
