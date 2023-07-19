#!/usr/bin/python3
''' Tests cases model for Base class '''
import unittest
from json import dumps, loads
from models.base import Base


class BaseTest(unittest.TestCase):
    ''' class for testing Base class '''

    def test__Base(self):
        ''' Test Base class initialisation without id '''
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test__baseIntId(self):
        ''' Test Base class initialisation with id of type int '''
        b1 = Base(99)
        self.assertEqual(b1.id, 99)

    def test__baseListId(self):
        ''' Test Base class initialisation with id of type list '''
        kwargs = {'id': [1, 2]}
        self.assertEqual(Base(**kwargs).id, [1, 2])

    def test__baseTypeError(self):
        ''' Test Base class initialisation type error '''
        self.assertRaises(TypeError, Base, *(1, 2))

    def test__baseToJsonString(self):
        ''' Test to_json_string() static method '''
        list_dictionaries = [{"id": 7}, {"id": 10}]
        self.assertEqual(dumps(list_dictionaries),
                Base.to_json_string(list_dictionaries))

    def test__baseToJsonStringEmptyList(self):
        ''' Test to_json_string() static method with empty list '''
        self.assertEqual('[]', Base.to_json_string([]))

    def test__baseToJsonStringNoneList(self):
        ''' Test to_json_string() static method with None type '''
        self.assertEqual('[]', Base.to_json_string(None))

    def test__baseToJsonStringTypeError(self):
        ''' Test to_json_string() static method without argument '''
        self.assertRaises(TypeError, Base.to_json_string)

    def test__baseFromJsonString(self):
        ''' Test from_json_string() static method with string '''
        list_dictionaries = [{"id": 7}, {"id": 10}]
        str1 = Base.to_json_string(list_dictionaries)
        self.assertEqual(list_dictionaries, Base.from_json_string(str1))

    def test__baseFromJsonEmptyString(self):
        ''' Test from_json_string() static method with empty string '''
        self.assertEqual([], Base.from_json_string(''))

    def test__baseFromJsonNoneString(self):
        ''' Test from_json_string() static method with None type '''
        self.assertEqual([], Base.from_json_string(None))

    def test__baseFromJsonStringTypeError(self):
        ''' Test from_json_string() static method without argument '''
        self.assertRaises(TypeError, Base.from_json_string)
