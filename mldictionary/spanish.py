"""Get Spanish meanings from dictionary's websites.

    Classes:
        Spanish
"""

from .dictionary import Dictionary


class Spanish(Dictionary):
    """Get word's meanings in Spanish from dle.rae.es/.

    ...

    Attributes:
        URL: str = 'https://dle.rae.es/{}?m=form'
            URL from a dictionary website replacing word's name to "{}"
        LANGUAGE: str = 'Spanish'
            Dictionary's language's name
        TARGET_TAG: str = 'p'
            HTML tag which has the meanings
        TARGET_ATTR: dict[str, str] = {'class': 'j'}
            Pair attribute: value which makes TARGET_TAG unique

    Methods:
        get_meanings(self, word: str) -> List[str]:
            return the word's meanings
    """

    URL = 'https://dle.rae.es/{}?m=form'
    TARGET_TAG = 'p'
    TARGET_ATTR = {'class': 'j'}
    LANGUAGE = 'Spanish'
    REPLACES = {}
