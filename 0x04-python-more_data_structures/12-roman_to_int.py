#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    if roman_string is None:
        return 0
    ro_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    value = 0
    for i in range(len(roman_string)):
        if i + 1 < len(roman_string) and ro_num[roman_string[i]] < ro_num[roman_string[i+1]]:
            value -= ro_num[roman_string[i]]
        else:
            value += ro_num[roman_string[i]]
    return value
