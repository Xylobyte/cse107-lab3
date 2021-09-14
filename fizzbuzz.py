"""
A program that prints out "Fizz" for multiples of 3 and "Buzz" for multiples of 5

file: fizzbuzz.py

author: Donovan Griego

Date: 9-13-2021

assignment: Lab 3
"""


def main():
    # Get upper limit from user
    upper = int(input("Enter a number: "))
    # Check input for invalidity
    if upper <= 0:
        print("Must be a positive integer")
    current = 1
    # Loop from 1 to upper limit
    while current <= upper:
        post_string = ""
        # Add strings to post string based on remainders
        if current % 3 == 0:
            post_string += "Fizz"
        if current % 5 == 0:
            post_string += "Buzz"
        # Print current number follwed by post string
        print("{} {}".format(current, post_string))
        current += 1


if __name__ == "__main__":
    main()
