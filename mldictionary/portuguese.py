"""Get Portuguese meanings from dictionary's websites.

    Classes:
        Portuguese
"""

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

    use_custom_soup = True

    def custom_soup(self, soup: BeautifulSoup) -> list[str]:
        _target_tag = meaning_tags = soup.find(
            self.target_tag, self.target_attr
        )

        if not _target_tag:
            return []

        meaning_tags = _target_tag.find_all('span')

        return [
            valid_meaning
            for valid_meaning in meaning_tags
            if 'class="cl"' not in str(valid_meaning)
            if 'class="etim"' not in str(valid_meaning)
            if not str(valid_meaning)[:17] == '<span class="tag"'
        ]
