#!/usr/bin/python3
def uppercase(str):
    upp_case = ""
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            upp_case = upp_case + chr(ord(str[i])-32)
        else:
            upp_case = upp_case + str[i]
    print("{:s}".format(upp_case))
