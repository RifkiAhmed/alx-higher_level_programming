#!/usr/bin/python3
''' Module for Base class
'''
import json


class Base:
    ''' Representing Base class '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Initialize instance '''
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        with open("Rectangle.json", encoding="utf-8", mode="w") as file:
            file.write(cls.to_json_string(list(
                cls.to_dictionary(ob) for ob in list_objs)))
