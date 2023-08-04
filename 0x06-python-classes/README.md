## ALX AFRICA SE Program

### **PROJECT: 0x06. Python - Classes and Objects <sup>`` Python `` `` OOP ``</sup>**
### **Learning objectives:**
 - Why Python programming is awesome
 - What is OOP
 - “first-class everything”
 - What is a class
 - What is an object and an instance
 - What is the difference between a class and an object or instance
 - What is an attribute
 - What are and how to use public, protected and private attributes
 - What is ``self``
 - What is a method
 - What is the special ``__init__`` method and how to use it
 - What is Data Abstraction, Data Encapsulation, and Information Hiding
 - What is a property
 - What is the difference between an attribute and a property in Python
 - What is the Pythonic way to write getters and setters in Python
 - dynamically create arbitrary new attributes for existing instances of a class
 - How to bind attributes to object and classes
 - What is the ``__dict__`` of a class and/or instance of a class and what does it contain
 - How does Python find the attributes of an object or class
 - How to use the ``getattr`` function

### **Instruction:**
> - You are not allowed to import any module

### **Tasks:**

#### **Task 0:** [0-square.py](0-square.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Write an empty class ``Square`` that defines a square

#### **Task 1:** [1-square.py](1-square.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Write a class ``Square`` that defines a square by: (based on [0-square.py](0-square.py))
> - Private instance attribute: ``size``
> - Instantiation with size (no type/value verification)

#### **Task 2:** [2-square.py](2-square.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Write a class ``Square`` that defines a square by: (based on [1-square.py](1-square.py))
> - Instantiation with optional size: ``def __init__(self, size=0):``
>   - size must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
>   - if size is less than 0, raise a ``ValueError`` exception with the message ``size must be >= 0``

#### **Task 3:** [3-square.py](3-square.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Write a class ``Square`` that defines a square by: (based on [2-square.py](2-square.py))
> - Public instance method: ``def area(self):`` that returns the current square area

#### **Task 4:** [4-square.py](4-square.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Write a class ``Square`` that defines a square by: (based on [3-square.py](3-square.py))
> - Private instance attribute: ``size``
>   - property ``def size(self):`` to retrieve it
>   - property setter ``def size(self, value):`` to set it:
>     - size must be an integer, otherwise raise a ``TypeError`` exception with the message ``size must be an integer``
>     - if size is less than 0, raise a ``ValueError`` exception with the message ``size must be >= 0``

#### **Task 5:** [5-square.py](5-square.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Write a class ``Square`` that defines a square by: (based on [4-square.py](4-square.py))
> - Public instance method: ``def my_print(self):`` that prints in stdout the square with the character ``#``:
>   - if size is equal to 0, print an empty line

#### **Task 6:** [6-square.py](6-square.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Write a class ``Square`` that defines a square by: (based on [5-square.py](5-square.py))
> - Private instance attribute: ``position``
>   - property ``def position(self)``: to retrieve it
>   - property setter ``def position(self, value):`` to set it:
>     - position must be a tuple of 2 positive integers, otherwise raise a ``TypeError`` exception with the message ``position must be a tuple of 2 positive integers``
> - Instantiation with optional size and optional position: ``def __init__(self, size=0, position=(0, 0)):``
> - Public instance method: ``def my_print(self):`` that prints in stdout the square with the character ``#``:
>   - if size is equal to 0, print an empty line
>   - position should be use by using space - Don’t fill lines by spaces when ``position[1] > 0``

#### **Task 7:** [100-singly_linked_list.py](100-singly_linked_list.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Write a class ``Node`` that defines a node of a singly linked list by:
> - Private instance attribute: ``data``
>   - property ``def data(self):`` to retrieve it
>   - property setter ``def data(self, value):`` to set it:
>     - data must be an integer, otherwise raise a ``TypeError`` exception with the message ``data must be an integer``
> - Private instance attribute: ``next_node``:
>   - property ``def next_node(self):`` to retrieve it
>   - property setter ``def next_node(self, value):`` to set it:
>     - next_node can be ``None`` or must be a ``Node``, otherwise raise a ``TypeError`` exception with the message ``next_node must be a Node object``
> - Instantiation with data and next_node: ``def __init__(self, data, next_node=None):``
> - And, write a class ``SinglyLinkedList`` that defines a singly linked list by:
> - Private instance attribute: ``head`` (no setter or getter)
> - Simple instantiation: ``def __init__(self):``
> - Should be printable:
>   - print the entire list in stdout
>   - one node number by line
> - Public instance method: ``def sorted_insert(self, value):`` that inserts a new Node into the correct sorted position in the list (increasing order)

#### **Task 8:** [101-square.py](101-square.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Write a class ``Square`` that defines a square by: (based on [6-square.py](6-square.py))
> - Printing a Square instance should have the same behavior as my_print()

#### **Task 9:** [102-square.py](102-square.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Write a class ``Square`` that defines a square by: (based on [4-square.py](4-square.py))
> - Square instance can answer to comparators: ``==``, ``!=``, ``>``, ``>=``, ``<`` and ``<=`` based on the square area

#### **Task 10:** [103-magic_class.py](103-magic_class.py) <sup>:green_circle:</sup> <!-- :computer:💻 :mag_right:🔎 :mag:🔍 :bulb:💡 -->
> - Write the Python class ``MagicClass`` that does exactly the same as the Python bytecode: click [here](103-magic_class.png)

### AUTHOR:
#### **Ahmed RIFKI** <sup>[@AhmedSeeker](https://github.com/AhmedSeeker)</sup>
