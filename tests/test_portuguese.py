import unittest

from .general_tests import GeneralTests
from mldictionary import Portuguese


class TestGeneralPortuguese(GeneralTests, unittest.TestCase):
    word = 'palavra'
    
    def setUp(self):
        return super().setUp(Portuguese)

class TestPortuguese(unittest.TestCase):
    def setUp(self):
        self.portuguese_dictionary = Portuguese()
