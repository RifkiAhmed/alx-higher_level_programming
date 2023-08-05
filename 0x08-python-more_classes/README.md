## ALX AFRICA SE Program

### **PROJECT: 0x08. Python - More Classes and Objects <sup>`` Python `` `` OOP ``</sup>**
### **Learning objectives:**
 - Why Python programming is awesome
 - What is OOP
 - “first-class everything”
 - What is a class
 - What is an object and an instance
 - What is the difference between a class and an object or instance
 - What is an attribute
 - What are and  - how to use public, protected and > - private attributes
 - What is ``self``
 - What is a method
 - What is the special ``__init__`` method and  - how to use it
 - What is Data Abstraction, Data Encapsulation, and Information Hiding
 - What is a property
 - What is the difference between an attribute and a > - property in Python
 - What is the Pythonic way to write getters and setters in Python
 - What are the special ``__str__`` and ``__repr__`` methods and  - how to use them
 - What is the difference between ``__str__`` and ``__repr__``
 - What is a class attribute
 - What is the difference between a object attribute and a class attribute
 - What is a class method
 - What is a static method
 - How to dynamically create arbitrary new attributes for existing instances of a class
 - How to bind attributes to object and classes
 - What is and  - what does contain ``__dict__`` of a class and of an instance of a class
 - How does Python find the attributes of an object or class
 - How to use the ``getattr`` function

### **Instruction:**
> - Not allowed to import any module

### **Tasks:**

#### [0-rectangle.py](0-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - An empty class ``Rectangle`` that defines a rectangle

#### [1-rectangle.py](1-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Rectangle`` that defines a rectangle by: (based on [0-rectangle.py](0-rectangle.py))
> - Private instance attribute: ``width``:
>   - property ``def width(self):`` to retrieve it
>   - property setter ``def width(self, value):`` to set it:
>     - width must be an integer, otherwise raise a ``TypeError`` exception with the message ``width must be an integer``
>     - if width is less than 0, raise a ``ValueError`` exception with the message ``width must be >= 0``
> - Private instance attribute: ``height``:
>   - property ``def height(self):`` to retrieve it
>   - property setter ``def height(self, value):`` to set it:
>     - height must be an integer, otherwise raise a ``TypeError`` exception with the message ``height must be an integer``
>     - if height is less than 0, raise a ``ValueError`` exception with the message ``height must be >= 0``
> - Instantiation with optional width and height: ``def __init__(self, width=0, height=0):``

#### [2-rectangle.py](2-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Rectangle`` that defines a rectangle by: (based on [1-rectangle.py](1-rectangle.py))
> - Public instance method: ``def area(self):`` that returns the rectangle area
> - Public instance method: ``def perimeter(self):`` that returns the rectangle perimeter:
>   - if width or height is equal to 0, perimeter is equal to 0

#### [3-rectangle.py](3-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Rectangle`` that defines a rectangle by: (based on [2-rectangle.py](2-rectangle.py))
> - ``print()`` and ``str()`` print the rectangle with the character ``#``:
>   - if width or height is equal to 0, return an empty string

#### [4-rectangle.py](4-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Rectangle`` that defines a rectangle by: (based on [3-rectangle.py](3-rectangle.py))
> - ``repr()`` return a string representation of the rectangle to be able to recreate a new instance by using ``eval()``

#### [5-rectangle.py](5-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Rectangle`` that defines a rectangle by: (based on [4-rectangle.py](4-rectangle.py))
> - Print the message ``Bye rectangle...`` (... being 3 dots not ellipsis) when an instance of Rectangle is deleted

#### [6-rectangle.py](6-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Rectangle`` that defines a rectangle by: (based on [5-rectangle.py](5-rectangle.py))
> - Public class attribute ``number_of_instances``:
>   - Initialized to 0
>   - Incremented during each new instance instantiation
>   - Decremented during each instance deletion

#### [7-rectangle.py](7-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Rectangle`` that defines a rectangle by: (based on [6-rectangle.py](6-rectangle.py))
> - Public class ``attribute print_symbol``:
>   - Initialized to #
>   - Used as symbol for string representation
>   - Can be any type

#### [8-rectangle.py](8-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Rectangle`` that defines a rectangle by: (based on [7-rectangle.py](7-rectangle.py))
> - Static method ``def bigger_or_equal(rect_1, rect_2):`` that returns the biggest rectangle based on the area
>   - rect_1 must be an instance of Rectangle, otherwise raise a ``TypeError`` exception with the message ``rect_1 must be an instance of Rectangle``
>   - rect_2 must be an instance of Rectangle, otherwise raise a ``TypeError`` exception with the message ``rect_2 must be an instance of Rectangle``
>   - Returns rect_1 if both have the same area value

#### [9-rectangle.py](9-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Rectangle`` that defines a rectangle by: (based on [8-rectangle.py](8-rectangle.py))
> - Class method ``def square(cls, size=0):`` that returns a new Rectangle instance with ``width == height == size``

### AUTHOR:
#### **Ahmed RIFKI** <sup>[@AhmedSeeker](https://github.com/AhmedSeeker)</sup>
