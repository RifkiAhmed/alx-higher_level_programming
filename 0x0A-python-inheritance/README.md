## ALX AFRICA SE Program

### **PROJECT: 0x0A. Python - Inheritance <sup>`` Python `` `` OOP `` `` Inheritance ``</sup>**
### **Learning objectives:**
 - Why Python programming is awesome
 - What is a superclass, baseclass or parentclass
 - What is a subclass
 - How to list all attributes and methods of a class or instance
 - When can an instance have new attributes
 - inherit class from another
 - define a class with multiple base classes
 - What is the default class every class inherit from
 - override a method or attribute inherited from the base class
 - Which attributes or methods are available by heritage to subclasses
 - What is the purpose of inheritance
 - What are, when and use ``isinstance``, ``issubclass``, type and ``super`` built-in functions



### **Tasks:**

#### [0-lookup.py](0-lookup.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Prototype: ``def lookup(obj):``
>   - function that returns the list of available attributes and methods of an object

#### [1-my_list.py](1-my_list.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``MyList`` that inherits from ``list``
> - Public instance method: ``def print_sorted(self):`` that prints the list, but sorted (ascending sort)
>   - assuming that all the elements of the list will be of type int
> - Test Cases: [1-my_list.txt](tests/1-my_list.txt)

#### [2-is_same_class.py](2-is_same_class.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Prototype: ``def is_same_class(obj, a_class):``
>   - function that returns True if the object is exactly an instance of the specified class ; otherwise False

#### [3-is_kind_of_class.py](3-is_kind_of_class.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Prototype: ``def is_kind_of_class(obj, a_class):``
>   - function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False

#### [4-inherits_from.py](4-inherits_from.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Prototype: ``def inherits_from(obj, a_class):``
>   - function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False

#### [5-base_geometry.py](5-base_geometry.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Defines an empty class ``BaseGeometry``

#### [6-base_geometry.py](6-base_geometry.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``BaseGeometry`` (task based on [5-base_geometry.py](5-base_geometry.py))
>   - public instance method: ``def area(self):`` that raises an ``Exception`` with the message ``area() is not implemented``

#### [7-base_geometry.py](7-base_geometry.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``BaseGeometry`` (task based on [6-base_geometry.py](6-base_geometry.py))
>   - Public instance method: ``def integer_validator(self, name, value):`` that validates value:
>       - assuming name is always a string
>       - if value is not an integer: raise a ``TypeError`` exception, with the message ``<name> must be an integer``
>       - if value is less or equal to 0: raise a ``ValueError`` exception with the message ``<name> must be greater than 0``
> - Test Cases: [7-base_geometry.txt](tests/7-base_geometry.txt)
#### [8-rectangle.py](8-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Rectangle`` that inherits from BaseGeometry ([7-base_geometry.py](7-base_geometry.py))
>   - Instantiation with width and height: ``def __init__(self, width, height):``
>     - width and height are private. No getter or setter
>     - width and height are positive integers, validated by ``integer_validator``

#### [9-rectangle.py](9-rectangle.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Rectangle`` that inherits from BaseGeometry (task based on [8-rectangle.py](8-rectangle.py))
>   - ``area()`` method implemented
>   - ``print()`` print, and ``str()`` return, the following rectangle description: ``[Rectangle] <width>/<height>``

#### [10-square.py](10-square.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Square`` that inherits from Rectangle ([9-rectangle.py](9-rectangle.py)):
>   - Instantiation with size: ``def __init__(self, size):``
>     - size is private. No getter or setter
>     - size is a positive integer, validated by ``integer_validator``
>     - the ``area()`` method implemented

#### [11-square.py](11-square.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``Square`` that inherits from Rectangle (task based on [10-square.py](10-square.py)).
>   - ``print()`` print, and ``str()`` return, the square description: ``[Square] <width>/<height>``

#### [100-my_int.py](100-my_int.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - class ``MyInt`` that inherits from int:
>   - MyInt is a rebel. MyInt has ``==`` and ``!=`` operators inverted

#### [101-add_attribute.py](101-add_attribute.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Prototype: ``def add_attribute(mc, name, value)``
>   - function that adds a new attribute to an object if it’s possible
>     - Raise a ``TypeError`` exception, with the message ``can't add new attribute`` if the object can’t have new attribute
>     - Not allowed to use ``try/except``


### AUTHOR:
#### **Ahmed RIFKI** <sup>[@AhmedSeeker](https://github.com/AhmedSeeker)</sup>
