import unittest

from mldictionary import Spanish


class TestSpanish(unittest.TestCase):
    def setUp(self):
        self.spanish_dictionary = Spanish()

    def test_attribute_URL_type(self):
        self.assertIsInstance(self.spanish_dictionary.URL, str)

    def test_attribute_LANGUAGE_type(self):
        self.assertIsInstance(self.spanish_dictionary.LANGUAGE, str)

    def test_attribute_TARGET_TAG_type(self):
        self.assertIsInstance(self.spanish_dictionary.TARGET_TAG, str)

    def test_attribute_TARGET_ATTR_type(self):
        self.assertIsInstance(self.spanish_dictionary.TARGET_ATTR, dict)

    def test_method__search_status_code(self):
        response = self.spanish_dictionary._search('palabra')
        self.assertEqual(response.status_code, 200)

    def test_method_get_meanings_return_type(self):
        self.assertIsInstance(self.spanish_dictionary.get_meanings('palabra'), list)

    def test_method_get_meanings_not_found_word_type(self):
        self.assertIsInstance(self.spanish_dictionary.get_meanings('jsh'), list)

    def test_method_get_meanings_return_content(self):
        is_all_content_valid = all(
            len(mean) > 0 for mean in self.spanish_dictionary.get_meanings('palabra')
        )
        self.assertTrue(is_all_content_valid)
