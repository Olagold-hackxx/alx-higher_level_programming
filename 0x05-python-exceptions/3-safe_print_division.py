#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        a/b
        return a/b
    except Exception:
        return None
    finally:
        if b != 0:
            print("Inside result: {}".format(a/b))
        else:
            print("Inside result: {}".format(None))
