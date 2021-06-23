import re
from typing import List, Union

from .dictionary import Dictionary

class Portuguese(Dictionary):
    URL = 'https://www.dicio.com.br/{}/'
    XPATH = '//p[@itemprop="description"]/span'
    LANGUAGE = 'Portuguese'
    
    @classmethod
    def _clean_html(cls, meanings_html: List[str])->Union[List[str], bool]:
        def clean_html_tags(mean: str)->str:
            if 'class="cl"' in mean or 'class="etim"' in mean:
                return '&&remove&&'
            return re.sub('<[^>]*>', '', mean)
        meanings = list(map(clean_html_tags, meanings_html))
        [meanings.remove('&&remove&&') for _ in range(meanings.count('&&remove&&'))]
        return meanings or False
