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
        URL: str = 'https://dictionary.cambridge.org/us/dictionary/english/{}'
            URL from a dictionary website replacing word's name to "{}"
        LANGUAGE: str = 'English'
            Dictionary's language's name
        TARGET_TAG: str = 'div'
            HTML tag which has the meanings
        TARGET_ATTR: dict[str, str] = {'class': 'ddef_d'}
            Pair attribute: value which makes TARGET_TAG unique

    Methods:
        get_meanings(self, word: str) -> List[str]:
            return the word's meanings
    """

    URL = 'https://dictionary.cambridge.org/us/dictionary/english/{}'
    TARGET_TAG = 'div'
    TARGET_ATTR = {'class': 'ddef_d'}
    LANGUAGE = 'English'
    REPLACES = {'\n': '', ' :': ':'}

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
