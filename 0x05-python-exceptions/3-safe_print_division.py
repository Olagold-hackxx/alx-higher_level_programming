#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a/b
        return a/b
    except:
        return None
    finally:
        if a != 0 and b != 0:
            print("Inside result: {}".format(a/b))
        else:
            print("Inside result: {}".format(None))
