"""Get English meanings from dictionary's websites.

Classes:
    English
"""
from typing import List

from .dictionary import Dictionary


class English(Dictionary):
    """Get word's meanings in English from cambridge.org.

    ...

    Attributes:
        url: str = 'https://dictionary.cambridge.org/us/dictionary/english/{}'
            URL from a dictionary website replacing word's name to "{}"
        language: str = 'English'
            Dictionary's language's name
        target_tag: str = 'div'
            HTML tag which has the meanings
        target_attr: dict[str, str] = {'class': 'ddef_d'}
            Pair attribute: value which makes TARGET_TAG unique

    Methods:
        get_meanings(self, word: str) -> List[str]:
            return the word's meanings
    """

    url = 'https://dictionary.cambridge.org/us/dictionary/english/{}'
    target_tag = 'div'
    target_attr = {'class': 'ddef_d'}
    language = 'English'
    replaces = {'\n': '', ' :': ':'}

    @classmethod
    def _replace_terms(cls, meanings: List[str]):
        formatted_meanings = []
        for meaning in meanings:
            meaning = meaning.strip()
            if not meaning[-1:].isalpha():
                formatted_meanings.append(meaning[:-1] + '.')
            else:
                formatted_meanings.append(meaning + '.')
        return super()._replace_terms(formatted_meanings)
