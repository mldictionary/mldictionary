from typing import Union
import unittest
from unittest import FunctionTestCase

from mldictionary import (
    English,
    Portuguese,
    Spanish
)

class GeneralTests():
    word: str
    invalid_word: str = 'djsfhkhjshdgdkhskdd'
    
    def setUp(self, language_class: Union[English, Portuguese, Spanish]):
        self.dictionary = language_class()

    def test_attribute_URL_type(self):
        self.assertIsInstance(self.dictionary.URL, str)

    def test_attribute_LANGUAGE_type(self):
        self.assertIsInstance(self.dictionary.LANGUAGE, str)

    def test_attribute_TARGET_TAG_type(self):
        self.assertIsInstance(self.dictionary.TARGET_TAG, str)

    def test_attribute_TARGET_ATTR_type(self):
        self.assertIsInstance(self.dictionary.TARGET_ATTR, dict)

    def test_attribute_REPLACES_type(self):
        self.assertIsInstance(self.dictionary.REPLACES, dict)

    def test_method__search_status_code(self):
        response = self.dictionary._search(self.word)
        self.assertEqual(response.status_code, 200)

    def test_method_get_meanings_return_type(self):
        self.assertIsInstance(self.dictionary.get_meanings(self.word), list)

    def test_method_get_meanings_not_found_word_type(self):
        not_found_meaning = self.dictionary.get_meanings(self.invalid_word)
        self.assertIsInstance(not_found_meaning, list)
        self.assertEqual(len(not_found_meaning), 0)

    def test_method_get_meanings_return_content(self):
        is_all_content_valid = all(
            len(mean) > 0 for mean in self.dictionary.get_meanings(self.word)
        )
        self.assertTrue(is_all_content_valid)