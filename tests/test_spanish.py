import unittest

from .general_tests import GeneralTests
from mldictionary import Spanish


class TestGeneralSpanish(GeneralTests, unittest.TestCase):
    word = 'palabra'

    def setUp(self):
        return super().setUp(Spanish)


class TestSpanish(unittest.TestCase):
    word = 'palabra'

    def setUp(self):
        self.spanish_dictionary = Spanish()

    def test_meanings_start(self):
        meanings = self.spanish_dictionary.get_meanings(self.word)
        is_meanings_starting_with_numeric = any(
            meaning[0].isdigit() for meaning in meanings
        )
        self.assertFalse(is_meanings_starting_with_numeric)
