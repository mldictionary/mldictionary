from typing import Union

from mldictionary import English, Portuguese, Spanish


class GeneralTests:
    word: str
    invalid_word: str = 'djsfhkhjshdgdkhskdd'

    def setUp(self, language_class: Union[English, Portuguese, Spanish]):
        self.dictionary = language_class()

    def test_attribute_url_type(self):
        self.assertIsInstance(self.dictionary.url, str)

    def test_attribute_language_type(self):
        self.assertIsInstance(self.dictionary.language, str)

    def test_attribute_target_tag_type(self):
        self.assertIsInstance(self.dictionary.target_tag, str)

    def test_attribute_target_attr_type(self):
        self.assertIsInstance(self.dictionary.target_attr, dict)

    def test_attribute_replaces_type(self):
        if hasattr(self.dictionary, 'replaces'):
            self.assertIsInstance(self.dictionary.replaces, dict)

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
        is_there_a_content = len(self.dictionary.get_meanings(self.word)) > 0
        self.assertTrue(is_there_a_content)
        is_all_content_valid = all(
            len(mean) > 0 for mean in self.dictionary.get_meanings(self.word)
        )
        self.assertTrue(is_all_content_valid)
