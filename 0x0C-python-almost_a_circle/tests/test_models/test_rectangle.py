#!/usr/bin/python3
''' Tests cases model for Rectangle class '''
import unittest
import os
from json import dumps, loads
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    ''' class of tests cases for testing Rectange class '''

    def setUp(self):
        ''' Defines variables and initialize instances '''
        self.args = [10, 20, 30, 40, 50, 60]
        self.kwargs = {'width': 1, 'height': 3, 'x': 5, 'y': 7, 'id': 99}
        self.r1 = Rectangle(*self.args[: 5])
        self.r2 = Rectangle(**self.kwargs)

        try:
            os.remove("Rectangle.json")
        except Exception:
            pass

        try:
            os.remove("Square.json")
        except Exception:
            pass

    def tearDown(self):
        ''' Removes variable '''
        del self.args, self.kwargs

    def test__init(self):
        ''' Test __init__() instance method '''
        self.assertEqual(Rectangle(1, 2).width, 1)
        self.assertEqual(Rectangle(1, 2).height, 2)
        self.assertEqual(Rectangle(1, 2).x, 0)
        self.assertEqual(Rectangle(1, 2).y, 0)

    def test__typeError(self):
        ''' Test instance type errors '''
        self.assertRaises(TypeError, Rectangle, *self.args[0: 0])
        self.assertRaises(TypeError, Rectangle, *self.args[0: 1])
        self.assertRaises(TypeError, Rectangle, *self.args)

    def test__width_ValueError(self):
        ''' Test width value errors '''
        self.assertRaises(ValueError, Rectangle, -10, 20, 30, 40, 50)
        self.assertRaises(ValueError, Rectangle, 0, 20, 30, 40, 50)

    def test__width_TypeError(self):
        ''' Test width type errors '''
        self.assertRaises(TypeError, Rectangle, 'w', 20, 30, 40, 50)
        self.assertRaises(TypeError, Rectangle, [1, 1, 1, 1], 20, 30, 40, 50)
        self.assertRaises(TypeError, Rectangle, None, 20, 30, 40, 50)

    def test__height_ValueError(self):
        ''' Test height value errors '''
        self.assertRaises(ValueError, Rectangle, 10, -20, 30, 40, 50)
        self.assertRaises(ValueError, Rectangle, 10, 0, 30, 40, 50)

    def test__height_TypeError(self):
        ''' Test  height type errors '''
        self.assertRaises(TypeError, Rectangle, 10, 'h', 30, 40, 50)
        self.assertRaises(TypeError, Rectangle, 10, [1, 1, 1, 1], 30, 40, 50)
        self.assertRaises(TypeError, Rectangle, 10, None, 30, 40, 50)

    def test__x_ValueError(self):
        ''' Test x value errors '''
        self.assertRaises(ValueError, Rectangle, 10, 20, -30, 40, 50)

    def test__x_TypeError(self):
        ''' Test x type errors '''
        self.assertRaises(TypeError, Rectangle, 10, 20, 'x', 40, 50)
        self.assertRaises(TypeError, Rectangle, 10, 20, [1, 1, 1, 1], 40, 50)
        self.assertRaises(TypeError, Rectangle, 10, 20, None, 40, 50)

    def test__y_ValueError(self):
        ''' Test y value errors '''
        self.assertRaises(ValueError, Rectangle, 10, 20, 30, -40, 50)

    def test__y_TypeError(self):
        ''' Test y type errors '''
        self.assertRaises(TypeError, Rectangle, 10, 20, 30, 'y', 50)
        self.assertRaises(TypeError, Rectangle, 10, 20, 30, [1, 1, 1, 1], 50)
        self.assertRaises(TypeError, Rectangle, 10, 20, 30, None, 50)

    def test__area(self):
        ''' Test area() instance method '''
        self.assertEqual(self.r1.area(), 200)
        self.assertIsInstance(self.r1.area(), int)

    def test__update(self):
        ''' Test update() instance method '''
        r6 = Rectangle(*self.args[: 5])
        r7 = Rectangle(**self.kwargs)
        self.r1.update(**self.kwargs)
        self.assertNotEqual(r6.width, self.r1.width)
        self.r2.update(*self.args[: 5])
        self.assertFalse(r7.id == self.r2.id)
        self.assertRaises(TypeError, Rectangle.update)
        self.assertRaises(AttributeError, Rectangle.update, None, None)
        Rectangle.update("welcome")
        self.assertRaises(AttributeError, Rectangle.update, *self.args)

    def test__to_Dictionary(self):
        ''' Test to_dictionary() instance method '''
        self.r1.update(**self.kwargs)
        d1 = self.r1.to_dictionary()
        self.assertEqual(d1, self.kwargs)
        self.assertIsInstance(d1, dict)
        self.assertRaises(TypeError, self.r1.to_dictionary, self.r2)
        self.assertRaises(AttributeError, Rectangle.to_dictionary, None)
        self.assertRaises(AttributeError, Rectangle.to_dictionary, "Hello")

    def test__str(self):
        ''' Test __str__() instance method '''
        s1 = '[Rectangle] (50) 30/40 - 10/20'
        self.assertTrue(s1 == str(self.r1))

    def test__toJsonString(self):
        ''' Test to_json_string() static method '''
        r1 = Rectangle(10, 7, 2, 48)
        list_dictionaries = r1.to_dictionary()
        self.assertEqual(
                dumps(list_dictionaries),
                Rectangle.to_json_string(list_dictionaries))

    def test__toJsonStringEmptyList(self):
        ''' Test to_json_string() static method '''
        self.assertEqual('[]', Rectangle.to_json_string([]))

    def test__toJsonStringNoneList(self):
        ''' Test to_json_string() static method '''
        self.assertEqual('[]', Rectangle.to_json_string(None))

    def test__toJsonStringTypeError(self):
        ''' Test to_json_string() static method '''
        self.assertRaises(TypeError, Rectangle.to_json_string)

    def test__fromJsonString(self):
        ''' Test from_json_string() static method '''
        r1 = Rectangle(10, 7, 2, 48)
        list_dictionaries = r1.to_dictionary()
        str1 = Rectangle.to_json_string(list_dictionaries)
        self.assertEqual(list_dictionaries, Rectangle.from_json_string(str1))

    def test__fromJsonEmptyString(self):
        ''' Test from_json_string() static method '''
        self.assertEqual([], Rectangle.from_json_string(''))

    def test__fromJsonNoneString(self):
        ''' Test from_json_string() static method '''
        self.assertEqual([], Rectangle.from_json_string(None))

    def test__fromJsonStringTypeError(self):
        ''' Test from_json_string() static method '''
        self.assertRaises(TypeError, Rectangle.from_json_string)

    def test__rectangleCreate(self):
        ''' Test create() instance method '''
        self.assertRaises(TypeError, Rectangle.create(**{'id': 89}))

    def test(self):
        ''' Test save_to_file() class method '''
        Rectangle.save_to_file(None)
        with open("Rectangle.json", encoding="utf-8", mode="r") as RectFile:
            self.assertEqual('[]', RectFile.read())
        Rectangle.save_to_file([])
        with open("Rectangle.json", encoding="utf-8", mode="r") as RectFile:
            self.assertEqual('[]', RectFile.read())
        rectangle1 = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([rectangle1])
        with open("Rectangle.json", encoding="utf-8", mode="r") as RectFile:
            str1 = Rectangle.to_json_string([rectangle1.to_dictionary()])
            self.assertEqual(str1, RectFile.read())
