#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    LastDigit = number % 10
    print(LastDigit, end="")
    return LastDigit
