import unittest

from mldictionary import English


class TestEnglish(unittest.TestCase):
    def setUp(self):
        self.english_dictionary = English()

    def test_attribute_URL_type(self):
        self.assertIsInstance(self.english_dictionary.URL, str)

    def test_attribute_LANGUAGE_type(self):
        self.assertIsInstance(self.english_dictionary.LANGUAGE, str)

    def test_attribute_TARGET_TAG_type(self):
        self.assertIsInstance(self.english_dictionary.TARGET_TAG, str)

    def test_attribute_TARGET_ATTR_type(self):
        self.assertIsInstance(self.english_dictionary.TARGET_ATTR, dict)

    def test_method_get_meanings_return_type(self):
        self.assertIsInstance(self.english_dictionary.get_meanings('word'), list)

    def test_method_get_meanings_return_content(self):
        is_all_content_valid = all(
            len(mean) > 0 for mean in self.english_dictionary.get_meanings('word')
        )
        self.assertTrue(is_all_content_valid)
