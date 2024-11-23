#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

FORMAT_STRING = "{} = {}"
roman_number = "X"
print(FORMAT_STRING.format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print(FORMAT_STRING.format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print(FORMAT_STRING.format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print(FORMAT_STRING.format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print(FORMAT_STRING.format(roman_number, roman_to_int(roman_number)))

