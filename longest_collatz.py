"""
A program that uses collatz.py to find the longest chain with a start under 1000000

file: longest_collatz.py

author: Donovan Griego

Date: 9-13-2021

assignment: Lab 3
"""
import collatz


def main():
    longest = [0, 0]
    print("Yes I'm running, give me a sec...")
    for i in range(1, 1000000):
        if collatz.collatz_len(i) > longest[1]:
            longest[0] = i
            longest[1] = collatz.collatz_len(i)
    print("Longest chain is produced by {} with a sequence length of {}.".format(
        longest[0], longest[1]))


if __name__ == "__main__":
    main()
