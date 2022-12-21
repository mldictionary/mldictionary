"""Module dictionary"""

import logging
import re
import unicodedata

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
    """

    url: str
    language: str
    target_tag: str
    target_attr: dict[str, str]
    replaces: dict[str, str]

    # define if it will use custom soup
    use_custom_soup: bool = False

    def __str__(self) -> str:
        """Return dictionary's language"""
        return self.language

    @classmethod
    def _search(cls, word: str) -> requests.models.Response:
        with requests.get(
            cls.url.format(word), headers={'User-Agent': 'Mozilla'}
        ) as response:
            return response

    def _replace_terms(self, meanings: list[str]) -> list[str]:
        """Replace the unwanted terms of meanings."""
        replaces = self.replaces if hasattr(self, 'replaces') else {}
        replaced_meanings = []
        for meaning in meanings:
            for from_it, to in replaces.items():
                meaning = meaning.replace(from_it, to)
            replaced_meanings.append(meaning)
        return replaced_meanings

    def _soup_meanings(self, html_tree: str) -> list[str]:
        try:
            soup = BeautifulSoup(html_tree, 'html.parser')

            if self.use_custom_soup:
                meaning_tags = self.custom_soup(soup)
            else:
                meaning_tags = soup.find_all(
                    self.target_tag, self.target_attr
                )

            # don't al low duplicated item
            return list(
               dict.fromkeys([meaning.get_text() for meaning in meaning_tags])
            )
        except:  # noqa: E722
            logging.exception(
                'An exception occur while souping meanings',
                exc_info=True
            )
            return []

    def custom_soup(self, soup: BeautifulSoup) -> list[str]:
        """Custom soup process"""

    def get_meanings(self, word: str) -> list[str]:
        """Return a list of meanings."""

        word = unicodedata.normalize('NFD', word)
        word = re.sub('[\u0300-\u036f]', '', word)
        search_word_response_html = self._search(word).text

        if len(meanings := self._soup_meanings(search_word_response_html)) > 0:
            replaced_meanings = self._replace_terms(meanings)
            return replaced_meanings
        else:
            return []
