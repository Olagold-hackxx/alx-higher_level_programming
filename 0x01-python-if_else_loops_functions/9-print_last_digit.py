#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = abs(number)
    last_digit = number % 10
    print(last_digit, end="")
    return last_digit
