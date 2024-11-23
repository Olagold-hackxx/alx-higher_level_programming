#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

FORMAT_STRING = "{:d} instances of Rectangle"

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print(FORMAT_STRING.format(Rectangle.number_of_instances))
del my_rectangle_1
print(FORMAT_STRING.format(Rectangle.number_of_instances))
del my_rectangle_2
print(FORMAT_STRING.format(Rectangle.number_of_instances))

