#!/usr/bin/python3
''' Module for Base class
'''
import json


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
        ''' Returns the JSON string representation of list_dictionaries '''
        if list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_instances):
        ''' Writes the JSON string representation of list_instances to a file
        '''
        with open("Rectangle.json", encoding="utf-8", mode="w") as file:
            file.write(cls.to_json_string(list(
                cls.to_dictionary(ob) for ob in list_instances)))

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of the JSON string representation json_string '''
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Loads instance from dictionary.'''
        from rectangle import Rectangle
        from square import Square

        instance = None
        if cls is Rectangle:
            instance = Rectangle(1, 1)
        elif cls is Square:
            instance = Square(1)
        instance.update(**dictionary)
        return instance
