#!/usr/bin/python3


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    string = ""
    if text == "":
        print(text, end="")
    for i in range(len(text)):
        if text[i] != ':' and text[i] != '.' and text[i] != '?' and text[i] != " ":
            string += text[i]
        elif text[i] == " ":
            continue
        else:
            string += text[i]
            print(string)
            print()
            string = ""
    print(string, end="")
