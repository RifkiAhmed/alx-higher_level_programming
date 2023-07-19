#!/usr/bin/python3
''' Tests cases model for Rectangle class '''
import unittest
import os
from json import dumps, loads
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    ''' class of tests cases for testing Rectangle class '''

    def setUp(self):
        ''' Defines variables and removes file Rectangle.json '''
        self.args = [10, 20, 30, 40, 50]
        self.kwargs = {'width': 1, 'height': 3, 'x': 5, 'y': 7, 'id': 99}
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

    def tearDown(self):
        ''' Removes variables and file Rectangle.json '''
        del self.args, self.kwargs
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

    def test__Rectangle(self):
        ''' Test Rectangle class initialisation '''
        self.assertEqual(Rectangle(1, 2).width, 1)
        self.assertEqual(Rectangle(1, 2).height, 2)
        self.assertEqual(Rectangle(1, 2).x, 0)
        self.assertEqual(Rectangle(1, 2).y, 0)

    def test__rectangleTypeError(self):
        ''' Test Rectangle class initialisation type error '''
        self.assertRaises(TypeError, Rectangle)

    def test__rectangleWidthValueError(self):
        ''' Test Rectangle instance width value errors '''
        self.assertRaises(ValueError, Rectangle, -10, 20)
        self.assertRaises(ValueError, Rectangle, 0, 20)

    def test__rectangleWidthTypeError(self):
        ''' Test Rectangle instance width type error '''
        self.assertRaises(TypeError, Rectangle, 'w', 20)

    def test__rectangleHeightValueError(self):
        ''' Test Rectangle instance width value errors '''
        self.assertRaises(ValueError, Rectangle, 10, -20)
        self.assertRaises(ValueError, Rectangle, 10, 0)

    def test__rectangleHeightTypeError(self):
        ''' Test Rectangle instance width type error '''
        self.assertRaises(TypeError, Rectangle, 10, 'h')

    def test__rectangle_X_ValueError(self):
        ''' Test Rectangle instance X value error '''
        self.assertRaises(ValueError, Rectangle, 10, 20, -30)

    def test__rectangle_X_TypeError(self):
        ''' Test Rectangle instance X type error '''
        self.assertRaises(TypeError, Rectangle, 10, 20, 'x')

    def test__rectangle_Y_ValueError(self):
        ''' Test Rectangle instance Y value error '''
        self.assertRaises(ValueError, Rectangle, 10, 20, 30, -40)

    def test__rectangle_Y_TypeError(self):
        ''' Test Rectangle instance Y type error '''
        self.assertRaises(TypeError, Rectangle, 10, 20, 30, 'y')

    def test__rectangleArea(self):
        ''' Test Rectangle instance area() method '''
        self.assertEqual(Rectangle(*self.args).area(), 200)

    def test__rectangleUpdate(self):
        ''' Test Rectangle instance update() method '''
        s1 = Rectangle(*self.args[: 5])
        s2 = Rectangle(**self.kwargs)
        s1.update(**self.kwargs)
        self.assertEqual(s1.width, s2.width)

    def test__rectangle_to_Dictionary(self):
        ''' Test Rectangle instance to_dictionary() method '''
        d1 = Rectangle(**self.kwargs).to_dictionary()
        self.assertEqual(d1, self.kwargs)

    def test__rectangleDisplayWithoutXY(self):
        ''' Test Rectangle instance display() method '''
        from contextlib import redirect_stdout
        r1 = Rectangle(5, 10)
        str1 = '\n' * r1.y + '\n'.join(
                [' ' * r1.x + '#' * r1.width] * r1.height) + '\n'
        with open("Rectangle.txt", encoding="utf-8", mode="w") as in_Text:
            with redirect_stdout(in_Text):
                r1.display()
        with open("Rectangle.txt", encoding="utf-8", mode="r") as out_Text:
            self.assertEqual(str1, out_Text.read())

    def test__rectangleDisplayWithXY(self):
        ''' Test Rectangle instance display() method '''
        from contextlib import redirect_stdout
        r1 = Rectangle(5, 10, 10, 20)
        str1 = '\n' * r1.y + '\n'.join(
                [' ' * r1.x + '#' * r1.width] * r1.height) + '\n'
        with open("Rectangle.txt", encoding="utf-8", mode="w") as in_Text:
            with redirect_stdout(in_Text):
                Rectangle.display(r1)
        with open("Rectangle.txt", encoding="utf-8", mode="r") as out_Text:
            self.assertEqual(str1, out_Text.read())

    def test__rectangle__str(self):
        ''' Test Rectangle instance __str__() method '''
        s1 = Rectangle(*self.args)
        output = '[Rectangle] (50) 30/40 - 10/20'
        self.assertTrue(output == str(s1))

    def test__rectangleToJsonString(self):
        ''' Test super to_json_string() static method '''
        s1 = Rectangle(10, 7, 2, 48)
        list_dictionaries = s1.to_dictionary()
        self.assertEqual(
                dumps(list_dictionaries),
                Rectangle.to_json_string(list_dictionaries))

    def test__rectangleToJsonStringEmptyList(self):
        ''' Test super to_json_string() static method '''
        self.assertEqual('[]', Rectangle.to_json_string([]))

    def test__rectangleToJsonStringNoneList(self):
        ''' Test super to_json_string() static method '''
        self.assertEqual('[]', Rectangle.to_json_string(None))

    def test__rectangleToJsonStringTypeError(self):
        ''' Test super to_json_string() static method '''
        self.assertRaises(TypeError, Rectangle.to_json_string)

    def test__rectangleFromJsonString(self):
        ''' Test super from_json_string() static method '''
        s1 = Rectangle(10, 7, 2, 48)
        list_dictionaries = s1.to_dictionary()
        str1 = Rectangle.to_json_string(list_dictionaries)
        self.assertEqual(list_dictionaries, Rectangle.from_json_string(str1))

    def test__rectangleFromJsonEmptyString(self):
        ''' Test super from_json_string() static method '''
        self.assertEqual([], Rectangle.from_json_string(''))

    def test__rectangleFromJsonNoneString(self):
        ''' Test super from_json_string() static method '''
        self.assertEqual([], Rectangle.from_json_string(None))

    def test__rectangleFromJsonStringTypeError(self):
        ''' Test super from_json_string() static method '''
        self.assertRaises(TypeError, Rectangle.from_json_string)

    def test__rectangleCreate(self):
        ''' Test super create() class method '''
        self.assertRaises(TypeError, Rectangle.create(**{'id': 89}))

    def test__rectangleSaveToFileNoneList(self):
        ''' Test super save_to_file() class method '''
        Rectangle.save_to_file(None)
        with open("Rectangle.json", encoding="utf-8", mode="r") as RectFile:
            self.assertEqual('[]', RectFile.read())

    def test__rectangleSaveToFileEmptyList(self):
        ''' Test super save_to_file() class method '''
        Rectangle.save_to_file([])
        with open("Rectangle.json", encoding="utf-8", mode="r") as RectFile:
            self.assertEqual('[]', RectFile.read())

    def test__rectangleSaveToFile(self):
        ''' Test super save_to_file() class method '''
        s1 = Rectangle(1, 2)
        Rectangle.save_to_file([s1])
        with open("Rectangle.json", encoding="utf-8", mode="r") as RectFile:
            str1 = Rectangle.to_json_string([s1.to_dictionary()])
            self.assertEqual(str1, RectFile.read())

    def test__rectangleLoadFromFileExist(self):
        ''' Test super load_from__file() class method '''
        s1 = Rectangle(1, 2)
        Rectangle.save_to_file([s1])
        self.assertNotEqual(s1, Rectangle.load_from_file())

    def test__rectangleLoadFromFileNotFound(self):
        ''' Test super load_from__file() class method '''
        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        self.assertEqual([], Rectangle.load_from_file())
