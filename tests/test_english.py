import unittest

from .general_tests import GeneralTests
from mldictionary import English



class TestGeneralEnglish(GeneralTests, unittest.TestCase):
    word = 'word'
    
    def setUp(self):
        return super().setUp(English)

class TestEnglish(unittest.TestCase):
    word: str = 'word'
    
    def setUp(self):
        self.english_dictionary = English()

    def test_if_there_is_new_line_in_meanings(self):
        there_is_new_line_in_meanings = any(
            '\n' in meaning for meaning in self.english_dictionary.get_meanings(self.word)
        )
        self.assertFalse(there_is_new_line_in_meanings)
