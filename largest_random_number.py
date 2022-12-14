#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in December 2022
# A program that finds the largest number from a list of ten random numbers

import random


def find_largest_number_array(number_array):
    # Finds the largest number from a list of ten random numbers

    largest_number = 0

    for counter in range(0, len(number_array)):
        if number_array[counter] > largest_number:
            largest_number = number_array[counter]

    return largest_number


def main():
    # Generates ten random numbers in an array and calls a function

    random_array = []

    for counter in range(0, 10):
        random_number = random.randint(0, 100)
        random_array.append(random_number)
        print("Random #{0} is {1}".format(counter + 1, random_number))
    largest_number_array = find_largest_number_array(random_array)
    print("\nThe largest number in this array is {}.".format(largest_number_array))

    print("\nDone.")


if __name__ == "__main__":
    main()
