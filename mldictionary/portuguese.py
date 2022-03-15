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
        url: str = 'https://www.dicio.com.br/{}/'
            URL from a dictionary website replacing word's name to "{}"
        language: str = 'Portuguese'
            Dictionary's language's name
        target_tag: str = 'p'
            HTML tag which has the meanings
        target_attr: dict[str, str] = {'itemprop': 'description'}
            Pair attribute: value which makes TARGET_TAG unique

    Methods:
        get_meanings(self, word: str) -> List[str]:
            return the word's meanings
    """

    url = 'https://www.dicio.com.br/{}/'
    target_tag = 'p'
    target_attr = {'itemprop': 'description'}
    language = 'Portuguese'

    @classmethod
    def _soup_meanings(cls, html_tree: str) -> List[str]:
        try:
            soup = BeautifulSoup(html_tree, 'html.parser')
            meaning_tags = soup.find(cls.target_tag, cls.target_attr).find_all('span')
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
