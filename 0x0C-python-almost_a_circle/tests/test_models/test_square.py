#!/usr/bin/python3
''' Tests cases model for Square class '''
import unittest
import os
from json import dumps, loads
from models.square import Square


class TestSquare(unittest.TestCase):
    ''' class of tests cases for testing Rectange class '''

    def setUp(self):
        ''' Defines variables and initialize instances '''
        self.args = [10, 20, 30, 40, 50]
        self.kwargs = {'size': 1, 'x': 5, 'y': 7, 'id': 99}
        self.s1 = Square(*self.args[: 4])
        self.s2 = Square(**self.kwargs)

    try:
        os.remove("Square.json")
    except Exception:
        pass

    def tearDown(self):
        ''' Removes variable '''
        del self.args, self.kwargs

    def test__Square(self):
        ''' Test __init__() instance method '''
        self.assertEqual(Square(1).width, 1)
        self.assertEqual(Square(1).height, 1)
        self.assertEqual(Square(1).x, 0)
        self.assertEqual(Square(1).y, 0)

    def test__SquareTypeError(self):
        ''' Test instance type errors '''
        self.assertRaises(TypeError, Square, *self.args[0: 0])
        self.assertRaises(TypeError, Square, *self.args)

    def test__Size_ValueError(self):
        ''' Test width value errors '''
        self.assertRaises(ValueError, Square, -10, 20, 30, 40)
        self.assertRaises(ValueError, Square, 0, 20, 30, 40)

    def test__Size_TypeError(self):
        ''' Test width type errors '''
        self.assertRaises(TypeError, Square, 'w', 20, 30, 40)

    def test__Square_x_ValueError(self):
        ''' Test x value errors '''
        self.assertRaises(ValueError, Square, 10, -20, 30, 40)

    def test__Square_x_TypeError(self):
        ''' Test x type errors '''
        self.assertRaises(TypeError, Square, 10, 'x', 30, 40)

    def test__Square_y_ValueError(self):
        ''' Test y value errors '''
        self.assertRaises(ValueError, Square, 10, 20, -30, 40)

    def test__Square_y_TypeError(self):
        ''' Test y type errors '''
        self.assertRaises(TypeError, Square, 10, 20, 'y', 40)

    def test__SquareArea(self):
        ''' Test area() instance method '''
        self.assertEqual(self.s1.area(), 100)

    def test__SquareUpdate(self):
        ''' Test update() instance method '''
        s6 = Square(*self.args[: 4])
        s7 = Square(**self.kwargs)
        self.s1.update(**self.kwargs)
        self.assertNotEqual(s6.width, self.s1.width)
        self.s2.update(*self.args[: 4])
        self.assertFalse(s7.id == self.s2.id)

    def test__square_to_Dictionary(self):
        ''' Test to_dictionary() instance method '''
        self.s1.update(**self.kwargs)
        d1 = self.s1.to_dictionary()
        self.assertEqual(d1, self.kwargs)

    def test__Square__str(self):
        ''' Test __str__() instance method '''
        output = '[Square] (40) 20/30 - 10'
        self.assertTrue(output == str(self.s1))

    def test__squareToJsonString(self):
        ''' Test to_json_string() static method '''
        s1 = Square(10, 7, 2, 48)
        list_dictionaries = s1.to_dictionary()
        self.assertEqual(
                dumps(list_dictionaries),
                Square.to_json_string(list_dictionaries))

    def test__squareToJsonStringEmptyList(self):
        ''' Test to_json_string() static method '''
        self.assertEqual('[]', Square.to_json_string([]))

    def test__squareToJsonStringNoneList(self):
        ''' Test to_json_string() static method '''
        self.assertEqual('[]', Square.to_json_string(None))

    def test__squareToJsonStringTypeError(self):
        ''' Test to_json_string() static method '''
        self.assertRaises(TypeError, Square.to_json_string)

    def test__squareFromJsonString(self):
        ''' Test from_json_string() static method '''
        s1 = Square(10, 7, 2, 48)
        list_dictionaries = s1.to_dictionary()
        str1 = Square.to_json_string(list_dictionaries)
        self.assertEqual(list_dictionaries, Square.from_json_string(str1))

    def test__squareFromJsonEmptyString(self):
        ''' Test from_json_string() static method '''
        self.assertEqual([], Square.from_json_string(''))

    def test__squareFromJsonNoneString(self):
        ''' Test from_json_string() static method '''
        self.assertEqual([], Square.from_json_string(None))

    def test__squareFromJsonStringTypeError(self):
        ''' Test from_json_string() static method '''
        self.assertRaises(TypeError, Square.from_json_string)

    def test__rectangleCreate(self):
        ''' Test create() instance method '''
        self.assertRaises(TypeError, Square.create(**{'id': 89}))

    def test__squareSaveToFileNoneList(self):
        ''' Test save_to_file() class method '''
        Square.save_to_file(None)
        with open("Square.json", encoding="utf-8", mode="r") as SquareFile:
            self.assertEqual('[]', SquareFile.read())

    def test__squareSaveToFileEmptyList(self):
        ''' Test save_to_file() class method '''
        Square.save_to_file([])
        with open("Square.json", encoding="utf-8", mode="r") as SquareFile:
            self.assertEqual('[]', SquareFile.read())

    def test__squareSaveToFile(self):
        ''' Test save_to_file() class method '''
        Square1 = Square(1)
        Square.save_to_file([Square1])
        with open("Square.json", encoding="utf-8", mode="r") as SquareFile:
            str1 = Square.to_json_string([Square1.to_dictionary()])
            self.assertEqual(str1, SquareFile.read())

    def test__SquareLoadFromFileExist(self):
        ''' Test load_from__file() class method '''
        Square1 = Square(1)
        Square.save_to_file([Square1])
        self.assertNotEqual(Square1, Square.load_from_file())

    def test__SquareLoadFromFileNotFound(self):
        ''' Test load_from__file() class method '''
        try:
            os.remove("Square.json")
        except Exception:
            pass
        self.assertEqual([], Square.load_from_file())
