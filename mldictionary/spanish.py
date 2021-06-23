import re
from typing import List, Union

from .dictionary import Dictionary

class Spanish(Dictionary):
    URL = 'https://www.wordreference.com/definicion/{}'
    XPATH = '//ol[@class="entry"]//li'
    LANGUAGE = 'Spanish'
    
    @classmethod
    def _clean_html(cls,  meanings_html: List[str])->Union[str, bool]:
        index = 0
        def text_formatter(mean: str)->str:
            nonlocal index
            index+=1
            mean = mean.replace('<br>', '\n\t\t')
            return f'{index}º: ' + re.sub('<[^>]*>', '', mean)
        return '\n\n'.join(list(map(text_formatter, meanings_html))) or False
