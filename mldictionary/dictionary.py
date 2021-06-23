from abc import ABC, abstractmethod
import unicodedata
import re
import requests
from typing import List, Union

from parsel import Selector

class Dictionary(ABC):
    URL: str = ''
    XPATH: str = ''
    LANGUAGE: str = ''
    
    def __str__(self)->str:
        return self.LANGUAGE

    
    @classmethod
    def _search(cls, word: str)->str:
        with requests.get(cls.URL.format(word), \
                            headers={'User-Agent': 'Mozilla'}) as response:
            return response.text
        
        
    @classmethod
    @abstractmethod
    def _clean_html(self, meanings_html: List[str])->Union[str, bool]:
        ...

        
    def get_meanings(self, word: str)->List[str]:
        word = unicodedata.normalize('NFD', word)
        word = re.sub('[\u0300-\u036f]', '', word)
        response = Selector(text=self._search(word))
        meanings_html = list(dict.fromkeys(response.xpath(self.XPATH).getall()))# don't allow duplicated item
        meanings = self._clean_html(meanings_html)
        return meanings
