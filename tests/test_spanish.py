import unittest

from .general_tests import GeneralTests
from mldictionary import Spanish


class TestGeneralSpanish(GeneralTests, unittest.TestCase):
    word = 'palabra'
    
    def setUp(self):
        return super().setUp(Spanish)

class TestSpanish(unittest.TestCase):
    def setUp(self):
        self.spanish_dictionary = Spanish()

