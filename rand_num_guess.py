#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Oct 17, 2023
# This program make you guess between 1 to 9

import random


def main():
    user_guess = int(input("Guess a number between 0 to 9: "))
    print("")

    correct_guess = random.randint(0, 9)

    if user_guess == correct_guess:
        # check if he guessed correctly
        print("You guessed correctly.")
    else:
        # check if he guessed correctly
        print("You guessed incorrectly, the number was {}".format(correct_guess))


if __name__ == "__main__":
    main()
