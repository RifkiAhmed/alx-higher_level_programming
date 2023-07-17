#!/usr/bin/python3
''' Tests cases model for Base class '''
import unittest
from json import dumps, loads
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class BaseTest(unittest.TestCase):
    ''' class for testing Base class '''

    def setUp(self):
        ''' Instanciates Base class '''
        self.base1 = Base(99)

    def tearDown(self):
        ''' Removes Base class instance '''
        del self.base1

    def test_id(self):
        ''' Test instance attribute "id" '''
        self.assertIsNotNone(self.base1.id)
        self.assertEqual(self.base1.id, 99)

    def test_init1(self):
        ''' Test __init__() with 2 args'''
        args = (1, 2)
        self.assertRaises(TypeError, Base, *args)

    def test_init2(self):
        ''' Test __init__() with one and two key words arguments '''
        kwargs = {'id': 12}
        self.assertIs(Base(**kwargs).id, 12)
        kwargs['dummy_arg'] = 1
        self.assertRaises(TypeError, Base, **kwargs)

    def test_instance(self):
        ''' Test Base instance type '''
        self.assertIsInstance(self.base1, Base)

    def test_eq(self):
        ''' Test two Base instances non equality '''
        base1 = Base()
        base2 = Base()
        self.assertFalse(base1 == base2)

    def test__to_json_string(self):
        ''' Test to_json_string() static method '''
        r1 = Rectangle(10, 7, 2, 8)
        d1 = r1.to_dictionary()
        self.assertEqual(dumps([d1]), Base.to_json_string([d1]))
        self.assertEqual('[]', Base.to_json_string([]))
        self.assertEqual('[]', Base.to_json_string(None))