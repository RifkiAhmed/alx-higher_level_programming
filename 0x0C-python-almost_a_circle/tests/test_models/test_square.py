#!/usr/bin/python3
''' Tests cases model for Square class '''
import unittest
from json import dumps, loads
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    ''' class of tests cases for testing Rectange class '''

    def setUp(self):
        ''' Defines variables and initialize instances '''
        self.args = [10, 20, 30, 40, 50]
        self.kwargs = {'size': 1, 'x': 5, 'y': 7, 'id': 99}
        self.s1 = Square(*self.args[: 4])
        self.s2 = Square(**self.kwargs)

    def tearDown(self):
        ''' Removes variable '''
        del self.args, self.kwargs

    def test__init(self):
        ''' Test __init__() instance method '''
        s3 = Square(*self.args[: 1])
        s4 = Square(*self.args[: 2])
        s5 = Square(*self.args[: 3])
        self.assertIsInstance(self.s1, Square)
        self.assertEqual(self.s2.id, 99)
        self.assertTrue(self.s1.width == self.s1.height)
        self.assertGreater(s5.width, 0)

    def test__typeError(self):
        ''' Test instance type errors '''
        self.assertRaises(TypeError, Square, *self.args[0: 0])
        self.assertRaises(TypeError, Square, *self.args)

    def test__width_ValueError(self):
        ''' Test width value errors '''
        self.assertRaises(ValueError, Square, -10, 20, 30, 40)
        self.assertRaises(ValueError, Square, 0, 20, 30, 40)

    def test__width_TypeError(self):
        ''' Test width type errors '''
        self.assertRaises(TypeError, Square, 'w', 20, 30, 40)

    def test__x_ValueError(self):
        ''' Test x value errors '''
        self.assertRaises(ValueError, Square, 10, -20, 30, 40)

    def test__x_TypeError(self):
        ''' Test x type errors '''
        self.assertRaises(TypeError, Square, 10, 'x', 30, 40)

    def test__y_ValueError(self):
        ''' Test y value errors '''
        self.assertRaises(ValueError, Square, 10, 20, -30, 40)

    def test__y_TypeError(self):
        ''' Test y type errors '''
        self.assertRaises(TypeError, Square, 10, 20, 'y', 40)

    def test__area(self):
        ''' Test area() instance method '''
        self.assertEqual(self.s1.area(), 100)

    def test__update(self):
        ''' Test update() instance method '''
        s6 = Square(*self.args[: 4])
        s7 = Square(**self.kwargs)
        self.s1.update(**self.kwargs)
        self.assertNotEqual(s6.width, self.s1.width)
        self.s2.update(*self.args[: 4])
        self.assertFalse(s7.id == self.s2.id)

    def test__to_Dictionary(self):
        ''' Test to_dictionary() instance method '''
        self.s1.update(**self.kwargs)
        d1 = self.s1.to_dictionary()
        self.assertEqual(d1, self.kwargs)

    def test__str(self):
        ''' Test __str__() instance method '''
        output = '[Square] (40) 20/30 - 10'
        self.assertTrue(output == str(self.s1))

    def test__toJsonString(self):
        ''' Test to_json_string() static method '''
        s1 = Square(10, 7, 2, 48)
        list_dictionaries = s1.to_dictionary()
        self.assertEqual(
                dumps(list_dictionaries),
                Square.to_json_string(list_dictionaries))

    def test__toJsonStringEmptyList(self):
        ''' Test to_json_string() static method '''
        self.assertEqual('[]', Square.to_json_string([]))

    def test__toJsonStringNoneList(self):
        ''' Test to_json_string() static method '''
        self.assertEqual('[]', Square.to_json_string(None))

    def test__toJsonStringTypeError(self):
        ''' Test to_json_string() static method '''
        self.assertRaises(TypeError, Square.to_json_string)

    def test__fromJsonString(self):
        ''' Test from_json_string() static method '''
        s1 = Square(10, 7, 2, 48)
        list_dictionaries = s1.to_dictionary()
        str1 = Square.to_json_string(list_dictionaries)
        self.assertEqual(list_dictionaries, Square.from_json_string(str1))

    def test__fromJsonEmptyString(self):
        ''' Test from_json_string() static method '''
        self.assertEqual([], Square.from_json_string(''))

    def test__fromJsonNoneString(self):
        ''' Test from_json_string() static method '''
        self.assertEqual([], Square.from_json_string(None))

    def test__fromJsonStringTypeError(self):
        ''' Test from_json_string() static method '''
        self.assertRaises(TypeError, Square.from_json_string)
