#!/usr/bin/python3
''' Module for Base class '''
from json import dumps, loads
from csv import writer, reader


class Base:
    ''' Representing Base class '''
    __nb_instanceects = 0

    def __init__(self, id=None):
        ''' Initialize instance '''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_instanceects += 1
            self.id = type(self).__nb_instanceects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns JSON string representation of list_dictionaries '''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_instances):
        ''' Writes JSON string representation of list_instances to a file '''
        filename = cls.__name__ + '.json'
        with open(filename, encoding='utf-8', mode='w') as file:
            file.write(cls.to_json_string(list(
                cls.to_dictionary(ob) for ob in list_instances)))

    @staticmethod
    def from_json_string(json_string):
        ''' Returns list of the JSON string representation json_string '''
        if json_string is None or json_string == '':
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Loads instance from dictionary '''
        from models.rectangle import Rectangle
        from models.square import Square

        instance = None
        if cls is Rectangle:
            instance = Rectangle(1, 1)
        elif cls is Square:
            instance = Square(1)
        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        ''' Imports a list of instances from file '''
        filename = cls.__name__ + '.json'
        try:
            with open(filename, encoding='utf-8', mode='r') as file:
                dict_list = Base.from_json_string(file.read())
                instances = list(cls.create(**dic) for dic in dict_list)
            return instances
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        ''' Serialize list of objects in CSV file '''
        from models.rectangle import Rectangle
        from models.square import Square

        filename = cls.__name__ + '.csv'
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [
                        [obj.id, obj.width, obj.height, obj.x, obj.y]
                        for obj in list_objs
                        ]
            elif cls is Square:
                list_objs = [
                        [obj.id, obj.size, obj.x, obj.y]
                        for obj in list_objs
                        ]
        with open(filename, encoding='utf-8', mode='w', newline='') as file:
            csvwriter = writer(file)
            csvwriter.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        ''' Deserialize CSV file '''
        from models.rectangle import Rectangle
        from models.square import Square

        filename = cls.__name__ + '.csv'
        with open(filename, encoding='utf-8', mode='r') as file:
            csvreader = reader(file)
            instances = []
            for row in csvreader:
                row = [int(item) for item in row]
                if cls is Rectangle:
                    dictionary = {
                            'id': row[0],
                            'width': row[1],
                            'height': row[2],
                            'x': row[3],
                            'y': row[4]
                            }
                elif cls is Square:
                    dictionary = {
                            'id': row[0],
                            'size': row[1],
                            'x': row[2],
                            'y': row[3]
                            }
                instances.append(cls.create(**dictionary))
            return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        ''' Opens a window and draws all the Rectangles and Squares '''
        from turtle import Turtle, Screen
        from random import random

        mylist = list_rectangles[:] + list_squares[:]
        if mylist is not None:
            turtle = Turtle()
            screen = Screen()
            screen.bgcolor("yellow")
            screen.title('Welcome to turtle drawings!')
            turtle.pen(
                    {
                        'fillcolor': 'orange',
                        'pensize': 5,
                        'resizemode': 'user',
                        'stretchfactor': (1, 1)
                    })
            turtle.shape('turtle')
            turtle.speed('slowest')
            for form in mylist:
                turtle.clear()
                turtle.penup()
                turtle.setpos(0, 0)
                turtle.pencolor(random(), random(), random())
                turtle.setposition(form.x, form.y)
                turtle.write(form)
                turtle.pendown()
                for i in [1, 2]:
                    turtle.fd(form.width)
                    turtle.rt(90)
                    turtle.fd(form.height)
                    turtle.rt(90)
            screen.exitonclick()
