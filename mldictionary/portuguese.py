import re
from typing import List, Union

from .dictionary import Dictionary

class Portuguese(Dictionary):
    URL = 'https://www.dicio.com.br/{}/'
    XPATH = '//p[@itemprop="description"]/span'
    LANGUAGE = 'Portuguese'
    
    @classmethod
    def _clean_html(cls, meanings_html: List[str])->Union[str, bool]:
        index = 0
        def text_formatter(mean: str)->str:
            nonlocal index
            if 'class="cl"' in mean or 'class="etim"' in mean:
                return ''
            index+=1
            return f'{index}º: ' + re.sub('<[^>]*>', '', mean) + '\n\n'
        return ''.join(list(map(text_formatter, meanings_html)))\
            .replace('&*remove*&', '') or False
