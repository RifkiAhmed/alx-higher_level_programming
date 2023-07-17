#!/usr/bin/python3
''' Tests cases model for Rectangle class '''
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    ''' class of tests cases for testing Rectange class '''

    def setUp(self):
        ''' Defines variables and initialize instances '''
        self.args = [10, 20, 30, 40, 50, 60]
        self.kwargs = {'width': 1, 'height': 3, 'x': 5, 'y': 7, 'id': 99}
        self.r1 = Rectangle(*self.args[: 5])
        self.r2 = Rectangle(**self.kwargs)

    def tearDown(self):
        ''' Removes variable '''
        del self.args, self.kwargs

    def test__init(self):
        ''' Test __init__() instance method '''
        r3 = Rectangle(*self.args[: 2])
        r4 = Rectangle(*self.args[: 3])
        r5 = Rectangle(*self.args[: 4])
        self.assertIsInstance(self.r1, Rectangle)
        self.assertEqual(self.r2.id, 99)
        self.assertTrue(self.r1.width == 10)
        self.assertGreater(r5.width, 0)

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

    def test__height_ValueError(self):
        ''' Test height value errors '''
        self.assertRaises(ValueError, Rectangle, 10, -20, 30, 40, 50)
        self.assertRaises(ValueError, Rectangle, 10, 0, 30, 40, 50)

    def test__height_TypeError(self):
        ''' Test  height type errors '''
        self.assertRaises(TypeError, Rectangle, 10, 'h', 30, 40, 50)

    def test__x_ValueError(self):
        ''' Test x value errors '''
        self.assertRaises(ValueError, Rectangle, 10, 20, -30, 40, 50)

    def test__x_TypeError(self):
        ''' Test x type errors '''
        self.assertRaises(TypeError, Rectangle, 10, 20, 'x', 40, 50)

    def test__y_ValueError(self):
        ''' Test y value errors '''
        self.assertRaises(ValueError, Rectangle, 10, 20, 30, -40, 50)

    def test__y_TypeError(self):
        ''' Test y type errors '''
        self.assertRaises(TypeError, Rectangle, 10, 20, 30, 'y', 50)

    def test__area(self):
        ''' Test area() instance method '''
        self.assertEqual(self.r1.area(), 200)

    def test__update(self):
        ''' Test update() instance method '''
        r6 = Rectangle(*self.args[: 5])
        r7 = Rectangle(**self.kwargs)
        self.r1.update(**self.kwargs)
        self.assertNotEqual(r6.width, self.r1.width)
        self.r2.update(*self.args[: 5])
        self.assertFalse(r7.id == self.r2.id)

    def test__to_Dictionary(self):
        ''' Test to_dictionary() instance method '''
        self.r1.update(**self.kwargs)
        d1 = self.r1.to_dictionary()
        self.assertEqual(d1, self.kwargs)

    def test__str(self):
        ''' Test __str__() instance method '''
        s1 = '[Rectangle] (50) 30/40 - 10/20'
        self.assertTrue(s1 == str(self.r1))