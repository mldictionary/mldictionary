import re
from typing import List, Union

from .dictionary import Dictionary

class Spanish(Dictionary):
    URL = 'https://www.wordreference.com/definicion/{}'
    XPATH = '//ol[@class="entry"]//li'
    LANGUAGE = 'Spanish'
    
    @classmethod
    def _clean_html(cls,  meanings_html: List[str])->Union[List[str], bool]:
        def text_formatter(mean: str)->str:
            mean = mean.replace('<br>', '\n\t\t')
            return re.sub('<[^>]*>', '', mean)
        return list(map(text_formatter, meanings_html)) or False
