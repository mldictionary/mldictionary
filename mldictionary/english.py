import re
from typing import List, Union

from .dictionary import Dictionary

class English(Dictionary):
    URL = 'https://dictionary.cambridge.org/us/dictionary/english/{}'
    XPATH = '//div[has-class("def", "ddef_d", "db")]'
    LANGUAGE = 'English'

    @classmethod
    def _clean_html(cls, meanings_html: List[str])->Union[str, bool]:
        index = 0
        def text_formatter(mean: str)->str:
            nonlocal index
            index += 1
            mean = mean.replace('\n    \t                ', '').replace(':', '.')
            return f'{index}°: ' + re.sub('<[^>]*>', '', mean)
        return '\n\n'.join(list(map(text_formatter, meanings_html)))\
            .replace('\n        \n         ', ':  ') or False

