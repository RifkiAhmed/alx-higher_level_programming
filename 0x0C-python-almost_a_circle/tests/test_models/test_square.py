#!/usr/bin/python3
''' Tests cases model for Square class '''
import unittest
import os
from json import dumps, loads
from models.square import Square


class TestSquare(unittest.TestCase):
    ''' class of tests cases for testing Square class '''

    def setUp(self):
        ''' Defines variables and removes file Square.json '''
        self.args = [10, 20, 30, 40]
        self.kwargs = {'size': 1, 'x': 5, 'y': 7, 'id': 99}

        try:
            os.remove("Square.json")
        except Exception:
            pass

    def tearDown(self):
        ''' Removes variables and file Square.json '''
        del self.args, self.kwargs
        try:
            os.remove("Square.json")
        except Exception:
            pass

    def test__Square(self):
        ''' Test Square class initialisation '''
        self.assertEqual(Square(1).width, 1)
        self.assertEqual(Square(1).height, 1)
        self.assertEqual(Square(1).x, 0)
        self.assertEqual(Square(1).y, 0)

    def test__squareTypeError(self):
        ''' Test Square class initialisation type error '''
        self.assertRaises(TypeError, Square)

    def test__squareSizeValueError(self):
        ''' Test Square instance width value errors '''
        self.assertRaises(ValueError, Square, -10)
        self.assertRaises(ValueError, Square, 0)

    def test__squareSizeTypeError(self):
        ''' Test Square instance width type error '''
        self.assertRaises(TypeError, Square, 'w', 20)

    def test__square_X_ValueError(self):
        ''' Test Square instance X value error '''
        self.assertRaises(ValueError, Square, 10, -20)

    def test__square_X_TypeError(self):
        ''' Test Square instance X type error '''
        self.assertRaises(TypeError, Square, 10, 'x')

    def test__square_Y_ValueError(self):
        ''' Test Square instance Y value error '''
        self.assertRaises(ValueError, Square, 10, 20, -30)

    def test__square_Y_TypeError(self):
        ''' Test Square instance Y type error '''
        self.assertRaises(TypeError, Square, 10, 20, 'y')

    def test__squareArea(self):
        ''' Test Square instance area() method '''
        self.assertEqual(Square(*self.args).area(), 100)

    def test__squareUpdate(self):
        ''' Test Square instance update() method '''
        s1 = Square(*self.args[: 4])
        s2 = Square(**self.kwargs)
        s1.update(**self.kwargs)
        self.assertEqual(s1.width, s2.width)

    def test__square_to_Dictionary(self):
        ''' Test Square instance to_dictionary() method '''
        d1 = Square(**self.kwargs).to_dictionary()
        self.assertEqual(d1, self.kwargs)

    def test__square__str(self):
        ''' Test Square instance __str__() method '''
        s1 = Square(*self.args)
        output = '[Square] (40) 20/30 - 10'
        self.assertTrue(output == str(s1))

    def test__squareToJsonString(self):
        ''' Test super to_json_string() static method '''
        s1 = Square(10, 7, 2, 48)
        list_dictionaries = s1.to_dictionary()
        self.assertEqual(
                dumps(list_dictionaries),
                Square.to_json_string(list_dictionaries))

    def test__squareToJsonStringEmptyList(self):
        ''' Test super to_json_string() static method '''
        self.assertEqual('[]', Square.to_json_string([]))

    def test__squareToJsonStringNoneList(self):
        ''' Test super to_json_string() static method '''
        self.assertEqual('[]', Square.to_json_string(None))

    def test__squareToJsonStringTypeError(self):
        ''' Test super to_json_string() static method '''
        self.assertRaises(TypeError, Square.to_json_string)

    def test__squareFromJsonString(self):
        ''' Test super from_json_string() static method '''
        s1 = Square(10, 7, 2, 48)
        list_dictionaries = s1.to_dictionary()
        str1 = Square.to_json_string(list_dictionaries)
        self.assertEqual(list_dictionaries, Square.from_json_string(str1))

    def test__squareFromJsonEmptyString(self):
        ''' Test super from_json_string() static method '''
        self.assertEqual([], Square.from_json_string(''))

    def test__squareFromJsonNoneString(self):
        ''' Test super from_json_string() static method '''
        self.assertEqual([], Square.from_json_string(None))

    def test__squareFromJsonStringTypeError(self):
        ''' Test super from_json_string() static method '''
        self.assertRaises(TypeError, Square.from_json_string)

    def test__squareCreate(self):
        ''' Test super create() class method '''
        self.assertRaises(TypeError, Square.create(**{'id': 89}))

    def test__squareSaveToFileNoneList(self):
        ''' Test super save_to_file() class method '''
        Square.save_to_file(None)
        with open("Square.json", encoding="utf-8", mode="r") as SquareFile:
            self.assertEqual('[]', SquareFile.read())

    def test__squareSaveToFileEmptyList(self):
        ''' Test super save_to_file() class method '''
        Square.save_to_file([])
        with open("Square.json", encoding="utf-8", mode="r") as SquareFile:
            self.assertEqual('[]', SquareFile.read())

    def test__squareSaveToFile(self):
        ''' Test super save_to_file() class method '''
        s1 = Square(1)
        Square.save_to_file([s1])
        with open("Square.json", encoding="utf-8", mode="r") as SquareFile:
            str1 = Square.to_json_string([s1.to_dictionary()])
            self.assertEqual(str1, SquareFile.read())

    def test__squareLoadFromFileExist(self):
        ''' Test super load_from__file() class method '''
        s1 = Square(1)
        Square.save_to_file([s1])
        self.assertNotEqual(s1, Square.load_from_file())

    def test__squareLoadFromFileNotFound(self):
        ''' Test super load_from__file() class method '''
        try:
            os.remove("Square.json")
        except Exception:
            pass
        self.assertEqual([], Square.load_from_file())
