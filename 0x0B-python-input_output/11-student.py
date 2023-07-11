#!/usr/bin/python3
''' Module for representing a Student class
'''


class Student:
    ''' Student class
    '''

    def __init__(self, first_name, last_name, age):
        ''' Initialize class instance
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Writes dictionary representation of current class instance
        '''
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for item in attrs:
                for key in self.__dict__:
                    if key == item:
                        dic[key] = self.__dict__[key]
            return dic

    def reload_from_json(self, json):
        ''' Replaces all attributes of the currnet class Student instance
        '''
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
