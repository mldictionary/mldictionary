import unicodedata
import re
import requests
from typing import List

from bs4 import BeautifulSoup

class Dictionary:
    
    URL: str
    LANGUAGE: str
    TARGET_TAG: str 
    TARGET_ATTR: dict[str, str]

    def __str__(self)->str:
        return self.LANGUAGE


    @classmethod
    def _search(cls, word: str)->str:
        with requests.get(cls.URL.format(word), \
                            headers={'User-Agent': 'Mozilla'}) as response:
            return response.text


    @classmethod
    def _soup_meanings(cls, html_tree: str)->List[str]:
        try:
            soup = BeautifulSoup(html_tree, 'html.parser')
            meaning_tags = soup.find_all(cls.TARGET_TAG, cls.TARGET_ATTR)
            return list(dict.fromkeys([mean.get_text() for mean in meaning_tags])) # don't allow duplicated item
        except:
            return []


    def get_meanings(self, word: str)->List[str]:
        word = unicodedata.normalize('NFD', word)
        word = re.sub('[\u0300-\u036f]', '', word)
        return self._soup_meanings(self._search(word))
