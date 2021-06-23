import re
from typing import List, Union

from .dictionary import Dictionary

class English(Dictionary):
    URL = 'https://dictionary.cambridge.org/us/dictionary/english/{}'
    XPATH = '//div[has-class("def", "ddef_d", "db")]'
    LANGUAGE = 'English'

    @classmethod
    def _clean_html(cls, meanings_html: List[str])->Union[List[str], bool]:
        def text_formatter(mean: str)->str:
            mean = mean.replace('\n    \t                ', '').replace(':', '.')\
                 .replace('\n        \n         ', ':  ')
            return re.sub('<[^>]*>', '', mean)
        return list(map(text_formatter, meanings_html)) or False

