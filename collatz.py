"""
A program that finds the collatz segence length given a starting number

file: collatz.py

author: Donovan Griego

Date: 9-13-2021

assignment: Lab 3
"""


def main():
    start = int(input("Enter a starting number: "))
    print("Length of Collatz sequence: {}".format(collatz_len(start)))


def collatz_len(num):
    """returns the Collatz sequence length when starting at num

    num: integer to start at
    """
    len = 1
    while num != 1:
        if num % 2 == 0:
            num /= 2
        elif num % 2 == 1:
            num = (3 * num) + 1
        else:
            print("An error occurred")
            exit(1)
        len += 1
    return len


if __name__ == "__main__":
    main()
