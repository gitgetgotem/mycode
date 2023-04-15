#!/usr/bin/env python3

def main():
    bottles = int(input("How many bottles should start on the wall? ")) + 1
    if bottles > 101:
        print("You should call (800) 839-1686 and get some help")           
    else:
        for x in range(bottles):
            bottles -= 1
            print(f"""{bottles} bottles of beer on the wall!
{bottles} bottles of beer! Take one down, pass it around!""")

if __name__ == "__main__":
    main()
