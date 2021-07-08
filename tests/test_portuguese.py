import unittest

from mldictionary import Portuguese


class TestPortuguese(unittest.TestCase):
    def setUp(self):
        self.portuguese_dictionary = Portuguese()

    def test_attribute_URL_type(self):
        self.assertIsInstance(self.portuguese_dictionary.URL, str)

    def test_attribute_LANGUAGE_type(self):
        self.assertIsInstance(self.portuguese_dictionary.LANGUAGE, str)

    def test_attribute_TARGET_TAG_type(self):
        self.assertIsInstance(self.portuguese_dictionary.TARGET_TAG, str)

    def test_attribute_TARGET_ATTR_type(self):
        self.assertIsInstance(self.portuguese_dictionary.TARGET_ATTR, dict)

    def test_method__search_status_code(self):
        response = self.portuguese_dictionary._search('palavra')
        self.assertEqual(response.status_code, 200)

    def test_method_get_meanings_return_type(self):
        self.assertIsInstance(self.portuguese_dictionary.get_meanings('palavra'), list)

    def test_method_get_meanings_not_found_word_type(self):
        not_found_meaning = self.portuguese_dictionary.get_meanings('jsh')
        self.assertIsInstance(not_found_meaning, list)
        self.assertEqual(len(not_found_meaning), 0)

    def test_method_get_meanings_return_content(self):
        is_all_content_valid = all(
            len(mean) > 0 for mean in self.portuguese_dictionary.get_meanings('palavra')
        )
        self.assertTrue(is_all_content_valid)
