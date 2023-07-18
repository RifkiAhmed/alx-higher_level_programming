#!/usr/bin/python3
''' Tests cases model for Base class '''
import unittest
from json import dumps, loads
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    ''' class for testing Base class '''

    def test__init__NoneId(self):
        ''' Test __init__() instance method'''
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test__init__IntId(self):
        ''' Test __init__() instance method'''
        b2 = Base(99)
        self.assertEqual(b2.id, 99)

    def test__init__TypeError(self):
        ''' Test __init__() instance method'''
        self.assertRaises(TypeError, Base, *(1, 2))

    def test__init_ListId(self):
        ''' Test __init__() instance method'''
        kwargs = {'id': [1, 2]}
        self.assertEqual(Base(**kwargs).id, [1, 2])

    def test__init__TypeError(self):
        ''' Test __init__() instance method'''
        self.assertRaises(TypeError, Base, *(1, 2))

    def test__toJsonString(self):
        ''' Test to_json_string() static method '''
        list_dictionaries = [{"id": 7}, {"id": 10}]
        self.assertEqual(
                dumps(list_dictionaries),
                Base.to_json_string(list_dictionaries))

    def test__toJsonStringEmptyList(self):
        ''' Test to_json_string() static method '''
        self.assertEqual('[]', Base.to_json_string([]))

    def test__toJsonStringNoneList(self):
        ''' Test to_json_string() static method '''
        self.assertEqual('[]', Base.to_json_string(None))

    def test__toJsonStringTypeError(self):
        ''' Test to_json_string() static method '''
        self.assertRaises(TypeError, Base.to_json_string)

    def test__fromJsonString(self):
        ''' Test from_json_string() static method '''
        list_dictionaries = [{"id": 7}, {"id": 10}]
        str1 = Base.to_json_string(list_dictionaries)
        self.assertEqual(list_dictionaries, Base.from_json_string(str1))

    def test__fromJsonEmptyString(self):
        ''' Test from_json_string() static method '''
        self.assertEqual([], Base.from_json_string(''))

    def test__fromJsonNoneString(self):
        ''' Test from_json_string() static method '''
        self.assertEqual([], Base.from_json_string(None))

    def test__fromJsonStringTypeError(self):
        ''' Test from_json_string() static method '''
        self.assertRaises(TypeError, Base.from_json_string)
