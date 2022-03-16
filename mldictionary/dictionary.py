"""Module dictionary"""

import unicodedata
import re
from typing import List

from bs4 import BeautifulSoup
import requests


class Dictionary:
    """Dictionary class to use as a base to build dictionaries.

    class attributes:
        url: str
            url from a dictionary website replacing word's name to "{}"
        language: str
            Dictionary's language's name
        target_tag: str
            HTML tag which has the meanings
        target_attr: dict[str, str]
            Pair attribute: value which makes TARGET_TAG unique

    Class public methods:
        get_meanings(self, word: str) -> List[str]:
            return the word's meanings

    Class private methods:
        def _search(cls, word: str) -> requests.models.Response:
            Searche the word's meanings and
            return a requests.models.Response from that
        def _soup_meanings(cls, html_tree: str) -> List[str]:
            Soup a HTML tree and find out all meanings specified
    """

    url: str
    language: str
    target_tag: str
    target_attr: dict[str, str]
    replaces: dict[str, str]

    def __str__(self) -> str:
        """Return dictionary's language"""
        return self.language

    @classmethod
    def _search(cls, word: str) -> requests.models.Response:
        with requests.get(
            cls.url.format(word), headers={'User-Agent': 'Mozilla'}
        ) as response:
            return response

    @classmethod
    def _replace_terms(cls, meanings: List[str]) -> List[str]:
        """Replace the unwanted terms of meanings."""
        replaces = cls.replaces if hasattr(cls, 'replaces') else {}
        replaced_meanings = []
        for meaning in meanings:
            for from_it, to in replaces.items():
                meaning = meaning.replace(from_it, to)
            replaced_meanings.append(meaning)
        return replaced_meanings

    @classmethod
    def _soup_meanings(cls, html_tree: str) -> List[str]:
        try:
            soup = BeautifulSoup(html_tree, 'html.parser')
            meaning_tags = soup.find_all(cls.target_tag, cls.target_attr)
            # don't allow duplicated item
            return list(dict.fromkeys([meaning.get_text() for meaning in meaning_tags]))
        except:
            return []

    def get_meanings(self, word: str) -> List[str]:
        """Return a list of meanings."""

        word = unicodedata.normalize('NFD', word)
        word = re.sub('[\u0300-\u036f]', '', word)
        search_word_response_html = self._search(word).text
        if len(meanings := self._soup_meanings(search_word_response_html)) > 0:
            replaced_meanings = self._replace_terms(meanings)
            return replaced_meanings
        else:
            return []
