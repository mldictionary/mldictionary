"""Get Portuguese meanings from dictionary's websites.

    Classes:
        Portuguese
"""

from typing import List

from bs4 import BeautifulSoup

from .dictionary import Dictionary


class Portuguese(Dictionary):
    """Get word's meanings in Portuguese from dicio.com.br.

    ...

    Attributes:
        URL: str = 'https://www.dicio.com.br/{}/'
            URL from a dictionary website replacing word's name to "{}"
        LANGUAGE: str = 'Portuguese'
            Dictionary's language's name
        TARGET_TAG: str = 'p'
            HTML tag which has the meanings
        TARGET_ATTR: dict[str, str] = {'itemprop': 'description'}
            Pair attribute: value which makes TARGET_TAG unique

    Methods:
        get_meanings(self, word: str) -> List[str]:
            return the word's meanings
    """

    URL = 'https://www.dicio.com.br/{}/'
    TARGET_TAG = 'p'
    TARGET_ATTR = {'itemprop': 'description'}
    LANGUAGE = 'Portuguese'
    REPLACES = {}

    @classmethod
    def _soup_meanings(cls, html_tree: str) -> List[str]:
        try:
            soup = BeautifulSoup(html_tree, 'html.parser')
            meaning_tags = soup.find(cls.TARGET_TAG, cls.TARGET_ATTR).find_all('span')
            cleaned_meanings = [
                valid_meaning
                for valid_meaning in meaning_tags
                if not 'class="cl"' in str(valid_meaning)
                if not 'class="etim"' in str(valid_meaning)
                if not str(valid_meaning)[:17] == '<span class="tag"'
            ]
            return list(
                dict.fromkeys([meaning.get_text() for meaning in cleaned_meanings])
            )
        except:
            return []
