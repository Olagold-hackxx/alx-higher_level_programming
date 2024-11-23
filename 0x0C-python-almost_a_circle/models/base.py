#!/usr/bin/python3
"""
 Module that manages id attribute in all your future classes and to avoid
duplicating the same code (by extension, same bugs)
"""
import json
import turtle
import csv
from os.path import exists


class Base:
    """
    Class Base will be the “base” of all other classes
    in this project. The goal of it is to manage id attribute in
    all your future classes and to avoid duplicating the
    same code (by extension, same bugs)
    Private class attribute XXX
    class constructor: def __init__(self, id=None)::
    if id is not None, assign the public instance attribute
    id with this argument value
    you can assume id is an integer and
    you don’t need to test the type of it
    otherwise, increment __nb_objects and assign
    the new value to the public instance attribute id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializing this class
        Args:
            id(int): Can be None, will be assigned else specified
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        list_dictionary = []
        with open(cls.__name__ + '.json', "w") as f:
            if list_objs is None:
                return f.write('[]')
            else:
                for i in list_objs:
                    list_dictionary.append(i.to_dictionary())
                return f.write(cls.to_json_string(list_dictionary))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        if not exists(filename):
            return []

        with open(filename, mode="r", encoding="utf-8") as f:
            json_string = f.read()
            dictionary = cls.from_json_string(json_string)
            instance = []
            for i in dictionary:
                instance.append(cls.create(**i))
            return instance.__str__

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize objects to csv file"""
        if not list_objs:  # if empty/None, save empty list
            list_objs = []

        dict_list = []
        for obj in list_objs:  # convert objs to dicts
            dict_list.append(obj.to_dictionary())

        keys = [[key for key in d.keys()] for d in dict_list]

        with open((cls.__name__ + '.csv'), mode='w',
                  newline='', encoding='utf-8') as f:
            dwriter = csv.DictWriter(f, fieldnames=keys[0])
            dwriter.writeheader()
            dwriter.writerows(dict_list)

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize objects from csv file"""
        try:
            obj_list = []
            dictionary = {}
            with open(cls.__name__ + '.csv', mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                keys = reader.__next__()
                for values in reader:
                    for key, value in zip(keys, values):
                        dictionary[key] = int(value)
                    obj_list.append(cls.create(**dictionary))
        except IOError:
            return []
        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangles and squares using Turtle graphics."""
        def initialize_turtle():
            """Set up the Turtle screen and return the Turtle instance."""
            tk = turtle.Screen()
            tk.bgcolor("green")  # background color
            tk.title("Turtle")   # window title
            tkp = turtle.Turtle()
            tkp.color("blue")    # object color
            return tkp

        def adjust_position(shape):
            """Ensure x and y values of a shape are within bounds."""
            if shape.x <= 5 or shape.y <= 5:
                shape.x, shape.y = 72, 5

        def draw_rectangle(tkp, rectangle):
            """Draw a rectangle with Turtle."""
            adjust_position(rectangle)
            for _ in range(rectangle.y):
                for _ in range(2):
                    tkp.forward(rectangle.width)
                    tkp.right(90)
                    tkp.forward(rectangle.height)
                    tkp.right(90)
                tkp.rt(rectangle.x)

        def draw_square(tkp, square):
            """Draw a square with Turtle."""
            adjust_position(square)
            for _ in range(square.y):
                for _ in range(4):
                    tkp.forward(square.size)
                    tkp.rt(90)
                tkp.rt(square.x)

        # Initialize Turtle
        tkp = initialize_turtle()

        # Draw rectangles
        for rectangle in list_rectangles:
            draw_rectangle(tkp, rectangle)

        # Change color and draw squares
        tkp.color("red")
        for square in list_squares:
            draw_square(tkp, square)

        turtle.done()
