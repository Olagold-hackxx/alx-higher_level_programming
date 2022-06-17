#!/sr/bin/python3


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    if text == "":
        print(text, end="")
    for i in range(len(text)):
        print(text[i], end="")
        if text[i] == "?" or text[i] == ":" or text[i] == ".":
            print()
            print()
