"""Get Spanish meanings from dictionary's websites.

    Classes:
        Spanish
"""
from typing import List

from .dictionary import Dictionary


class Spanish(Dictionary):
    """Get word's meanings in Spanish from dle.rae.es/.

    ...

    Attributes:
        url: str = 'https://dle.rae.es/{}?m=form'
            URL from a dictionary website replacing word's name to "{}"
        language: str = 'Spanish'
            Dictionary's language's name
        target_tag: str = 'p'
            HTML tag which has the meanings
        target_attr: dict[str, str] = {'class': 'j'}
            Pair attribute: value which makes TARGET_TAG unique

    Methods:
        get_meanings(self, word: str) -> List[str]:
            return the word's meanings
    """

    url = 'https://dle.rae.es/{}?m=form'
    target_tag = 'p'
    target_attr = {'class': 'j'}
    language = 'Spanish'
    replaces = {}

    @classmethod
    def _replace_terms(cls, meanings: List[str]):
        meanings = [meaning[6:].strip() for meaning in meanings]
        return super()._replace_terms(meanings)
