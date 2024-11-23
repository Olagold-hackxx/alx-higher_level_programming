# **Python - Inheritance**
##  Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
Why Python programming is awesome.  
What is a superclass, baseclass or parentclass.  
What is a subclass  
How to list all attributes and methods of a class or instance  
When can an instance have new attributes  
How to inherit class from another  
How to define a class with multiple base classes  
What is the default class every class inherit from  
How to override a method or attribute inherited from the base class  
Which attributes or methods are available by heritage to subclasses  
What is the purpose of inheritance  
What are, when and how to use isinstance, issubclass, type and super built-in functions  

**TASKS**  
1. Write a function that returns the list of available attributes and methods of an object:

    *  Prototype: def lookup(obj):  
    * You are not allowed to import any module
    *  File: 0-lookup.py

            guillaume@ubuntu:~/0x0A$ cat 0-main.py   
            #!/usr/bin/python3  
            lookup = \__import\__('0-lookup').lookup  
            class MyClass1(object):  
              pass

            class MyClass2(object):
            my_attr1 = 3
            def my_meth(self):  
              pass

            print(lookup(MyClass1))  
            print(lookup(MyClass2))  
            print(lookup(int))

            guillaume@ubuntu:~/0x0A$ ./0-main.py
            ['\__class\__', '\__delattr\__', '\__dict\__', '\__dir\__', '\__doc\__', '\__eq\__',   
            '\__format\__', '\__ge\__',  '\__getattribute\__', '\__gt\__', '\__hash\__', '\__init\__', '\__le\__', '\__lt\__',   
            '\__module\__', '\__ne\__', '\__new\__'  '\__reduce\__', '\__reduce_ex\__', '\__repr\__', '\__setattr\__', '\__sizeof\__', '\__str\__', '\__subclasshook\__', '\__weakref\__']  
            ['\__class\__', '\__delattr\__', '\__dict\__',     '\__dir\__', '\__doc\__'  '\__eq\__', '\__format\__', '\__ge\__'  '\__getattribute\__', '\__gt\__', '\__hash\__'  
            '\__init\__', '\__le\__', '\__lt\__', '\__module\__', '\__ne\__', '\__new\__'  '\__reduce\__', '\__reduce_ex\__', '\__repr\__',   
            '\__setattr\__', '\__sizeof\__', '\__str\__', '\__subclasshook\__', '\__weakref\__', 'my_attr1', 'my_meth']  
            ['\__abs\__', '\__add\__', '\__and\__', '\__bool\__', '\__ceil\__', '\__class\__', '\__delattr\__', '\__dir\__', '\__divmod\__',   '\__doc\__', '\__eq\__', '\__float\__',   '\__floor\__', '\__floordiv\__', '\__format\__', 
            '\__ge\__', '\__getattribute\__',   '\__getnewargs\__', '\__gt\__', '\__hash\__', '\__index\__', '\__init\__', '\__int\__', '\__invert\__', '\__le\__', '\__lshift\__',     
            '\__lt\__', '\__mod\__', '\__mul\__', '\__ne\__', '\__neg\__', '\__new\__', '\__or\__', '\__pos\__', '\__pow\__',   '\__radd\__', '\__rand\__', '\__rdivmod\__',   
            '\__reduce\__', '\__reduce_ex\__', '\__repr\__', '\__rfloordiv\__', '\__rlshift\__',  '\__rmod\__', '\__rmul\__', '\__ror\__',   '\__round\__', '\__rpow\__', '\__rrshift\__',
            '\__rshift\__', '\__rsub\__', '\__rtruediv\__',   '\__rxor\__', '\__setattr\__', '\__sizeof\__', '\__str\__', '\__sub\__', '\__subclasshook\__', '\__truediv\__', '\__trunc\__', '\__xor\__', 
            'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']  
            guillaume@ubuntu:~/0x0A$ 

2. Write a class MyList that inherits from list:

   * Public instance method: def print_sorted(self): that prints the list, but sorted (ascending sort)
   * You can assume that all the elements of the list will be of type int
   *  You are not allowed to import any module
   * File: 1-my_list.py, tests/1-my_list.txt  
  
          guillaume@ubuntu:~/0x0A$ cat 1-main.py  
          #!/usr/bin/python3  
          MyList = \__import\__('1-my_list').MyList
          my_list = MyList()  
          my_list.append(1)  
          my_list.append(4)  
          my_list.append(2)  
          my_list.append(3)  
          my_list.append(5)  
          print(my_list)  
          my_list.print_sorted()  
          print(my_list)  
          guillaume@ubuntu:~/0x0A$ ./1-main.py  
          [1, 4, 2, 3, 5]  
          [1, 2, 3, 4, 5]  
          [1, 4, 2, 3, 5]  
          guillaume@ubuntu:~/0x0A$ 
3. Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False.

   *  Prototype: def is_same_class(obj, a_class):
    * You are not allowed to import any module
    * File: 2-is_same_class.py

          guillaume@ubuntu:~/0x0A$ cat 2-main.py
          #!/usr/bin/python3
          is_same_class = \__import\__('2-is_same_class').is_same_class

          a = 1
          if is_same_class(a, int):
          print("{} is an instance of the class {}".format(a, int.\__name\__))
          if is_same_class(a, float):
            print("{} is an instance of the class {}".format(a, float.\__name\__))
          if is_same_class(a, object):
            print("{} is an instance of the class {}".format(a, object.\__name\__))
          guillaume@ubuntu:~/0x0A$ ./2-main.py
          1 is an instance of the class int
          guillaume@ubuntu:~/0x0A$ 


4. Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False.

   * Prototype: def is_kind_of_class(obj, a_class):
   * You are not allowed to import any module
   *  File: 3-is_kind_of_class.py

          guillaume@ubuntu:~/0x0A$ cat 3-main.py
          #!/usr/bin/python3
          is_kind_of_class = \__import\__('3-is_kind_of_class').is_kind_of_class

          a = 1
          if is_kind_of_class(a, int):
            print("{} comes from {}".format(a, int.\__name\__))
          if is_kind_of_class(a, float):
            print("{} comes from {}".format(a, float.\__name\__))
          if is_kind_of_class(a, object):
            print("{} comes from {}".format(a, object.\__name\__))

          guillaume@ubuntu:~/0x0A$ ./3-main.py
          1 comes from int
          1 comes from object
          guillaume@ubuntu:~/0x0A$ 

5. Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False.

    * Prototype: def inherits_from(obj, a_class):  
    * You are not allowed to import any module
  
          guillaume@ubuntu:~/0x0A$ cat 4-main.py
          #!/usr/bin/python3
          inherits_from = \__import\__('4-inherits_from').inherits_from

          a = True
          if inherits_from(a, int):
            print("{} inherited from class {}".format(a, int.\__name\__))
          if inherits_from(a, bool):
            print("{} inherited from class {}".format(a, bool.\__name\__))
          if inherits_from(a, object):
            print("{} inherited from class {}".format(a, object.\__name\__))

          guillaume@ubuntu:~/0x0A$ ./4-main.py
          True inherited from class int
          True inherited from class object
          guillaume@ubuntu:~/0x0A$ 


6. Write an empty class BaseGeometry.

     * You are not allowed to import any module
     * File: 5-base_geometry.py

           guillaume@ubuntu:~/0x0A$ cat 5-main.py  
           #!/usr/bin/python3
           BaseGeometry = \__import\__('5-base_geometry').BaseGeometry

           bg = BaseGeometry()

           print(bg)
           print(dir(bg))
           print(dir(BaseGeometry))

           guillaume@ubuntu:~/0x0A$ ./5-main.py
           <5-base_geometry.BaseGeometry object at 0x7f2050c69208>
           ['\__class\__', '\__delattr\__', '\__dict\__', '\__dir\__', '\__doc\__', '\__eq\__', '\__format\__', '\__ge\__', '\__getattribute\__', '\__gt\__', '\__hash\__', '\__init\__', '\__le\__', 
           '\__lt\__', '\__module\__', '\__ne\__', '\__new\__', '\__reduce\__', '\__reduce_ex\__', '\__repr\__', '\__setattr\__', '\__sizeof\__', '\__str\__', '\__subclasshook\__', '\__weakref\__']
           ['\__class\__', '\__delattr\__', '\__dict\__', '\__dir\__', '\__doc\__', '\__eq\__', '\__format\__', '\__ge\__', '\__getattribute\__', '\__gt\__', '\__hash\__', '\__init\__', '\__le\__', 
           '\__lt\__', '\__module\__', '\__ne\__', '\__new\__', '\__reduce\__', '\__reduce_ex\__', '\__repr\__', '\__setattr\__', '\__sizeof\__', '\__str\__', '\__subclasshook\__', '\__weakref\__']
           guillaume@ubuntu:~/0x0A$ 


7. Write a class BaseGeometry (based on 5-base_geometry.py).

      *  Public instance method: def area(self): that raises an Exception with the message area() is not implemented
      *  You are not allowed to import any module  
      *  File: 6-base_geometry.py

             guillaume@ubuntu:~/0x0A$ cat 6-main.py
             #!/usr/bin/python3
             BaseGeometry = \__import\__('6-base_geometry').BaseGeometry

             bg = BaseGeometry()

             try:
              print(bg.area())
             except Exception as e:
              print("[{}] {}".format(e.\__class\__.\__name\__, e))

             guillaume@ubuntu:~/0x0A$ ./6-main.py
             [Exception] area() is not implemented
             guillaume@ubuntu:~/0x0A$ 


8. Write a class BaseGeometry (based on 6-base_geometry.py).

     * Public instance method: def area(self): that raises an Exception with the message area() is not implemented  
     * Public instance method: def integer_validator(self, name, value): that validates value:  
          * you can assume name is always a string
          * if value is not an integer: raise a TypeError exception, with the message <name> must be an integer  
          * if value is less or equal to 0: raise a ValueError exception with the message <name> must be greater than 0  
      * You are not allowed to import any module
      * Files: 7-base_geometry.py, tests/7-base_geometry.txt

            guillaume@ubuntu:~/0x0A$ cat 7-main.py
            #!/usr/bin/python3
            BaseGeometry = \__import\__('7-base_geometry').BaseGeometry

            bg = BaseGeometry()

            bg.integer_validator("my_int", 12)
            bg.integer_validator("width", 89)

            try:
              bg.integer_validator("name", "John")
            except Exception as e:
              print("[ {}] {}".format(e.\__class\__.\__name\__, e))

            try:
              bg.integer_validator("age", 0)
            except Exception as e:
              print("[{}] {}".format(e.\__class\__.\__name\__, e))

            try:
              bg.integer_validator("distance", -4)
            except Exception as e:
              print("[{}] {}".format(e.\__class\__.\__name\__, e))

            guillaume@ubuntu:~/0x0A$ ./7-main.py  
            [TypeError] name must be an integer 
            [ValueError] age must be greater than 0  
            [ValueError] distance must be greater than 0
            guillaume@ubuntu:~/0x0A$ 

9. Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py).

     * Instantiation with width and height: def \__init\__(self, width, height):  
          * width and height must be private. No getter or setter  
         * width and height must be positive integers, validated by integer_validator  
     * File: 8-rectangle.py

           guillaume@ubuntu:~/0x0A$ cat 8-main.py  
           #!/usr/bin/python3
           Rectangle = \__import\__('8-rectangle').Rectangle

           r = Rectangle(3, 5)

           print(r)
           print(dir(r))

           try:
            print("Rectangle: {} - {}".format(r.width, r.height))
           except Exception as e:
            print("[{}] {}".format(e.\__class\__.\__name\__, e))

           try:
            r2 = Rectangle(4, True)
           except Exception as e:
            print("[{}] {}".format(e.\__class\__.\__name\__, e))

           guillaume@ubuntu:~/0x0A$ ./8-main.py
           <8-rectangle.Rectangle object at 0x7f6f488f7eb8>
           ['_Rectangle\__height', '_Rectangle\__width', '\__class\__', '\__delattr\__', '\__dict\__', '\__dir\__', '\__doc\__', '\__eq\__', '\__format\__', '\__ge\__', '\__getattribute\__', '\__gt\__', '\__hash\__', '\__init\__', 
           '\__le\__', '\__lt\__', '\__module\__', '\__ne\__', '\__new\__', '\__reduce\__', '\__reduce_ex\__', '\__repr\__', '\__setattr\__', '\__sizeof\__', '\__str\__', '\__subclasshook\__', '\__weakref\__', 'area', 'integer_validator']
           [AttributeError] 'Rectangle' object has no attribute 'width'
           [TypeError] height must be an integer

10. Write a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py)  

      * Instantiation with width and height: def \__init\__(self, width, height):  
        * width and height must be private. No getter or setter  
        * width and height must be positive integers validated by integer_validator  
        * the area() method must be implemented
        * print() should print, and str() should return, the following rectangle description: [Rectangle] <width>/<height>  
    *  File: 9-rectangle.py
  
           guillaume@ubuntu:~/0x0A$ cat 9-main.py
           #!/usr/bin/python3
           Rectangle = \__import\__('9-rectangle').Rectangle

           r = Rectangle(3, 5)

           print(r)
           print(r.area())

           guillaume@ubuntu:~/0x0A$ ./9-main.py
           [Rectangle] 3/5
           15
           guillaume@ubuntu:~/0x0A$ 

11. Write a class Square that inherits from Rectangle (9-rectangle.py):

     * Instantiation with size: def \__init\__(self, size):  
        * size must be private. No getter or setter  
        * size must be a positive integer, validated by integer_validator  
        * the area() method must be implemented  
      * File: 10-square.py

            guillaume@ubuntu:~/0x0A$ cat 10-main.py
            #!/usr/bin/python3
            Square = \__import\__('10-square').Square

            s = Square(13)

            print(s)
            print(s.area())

            guillaume@ubuntu:~/0x0A$ ./10-main.py
            [Rectangle] 13/13
            169
            guillaume@ubuntu:~/0x0A$ 


12. Write a class Square that inherits from Rectangle (9-rectangle.py). (task based on 10-square.py).

     * Instantiation with size: def \__init\__(self, size):  
          * size must be private. No getter or setter  
          * size must be a positive integer, validated by integer_validator  
          * the area() method must be implemented
          * print() should print, and str() should return, the square description: [Square] <width>/<height>  
      * File: 11-square.py

            guillaume@ubuntu:~/0x0A$ cat 11-main.py
            #!/usr/bin/python3
            Square = \__import\__('11-square').Square

            s = Square(13)

            print(s)
            print(s.area())

            guillaume@ubuntu:~/0x0A$ ./11-main.py
            [Square] 13/13
            169
            guillaume@ubuntu:~/0x0A$ 
