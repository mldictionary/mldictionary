from typing import List

from bs4 import BeautifulSoup

from .dictionary import Dictionary

class Portuguese(Dictionary):
    URL = 'https://www.dicio.com.br/{}/'
    TARGET_TAG = 'p'
    TARGET_ATTR = {'itemprop': 'description'}
    XPATH = '//p[@itemprop="description"]/span'
    LANGUAGE = 'Portuguese'
    
    @classmethod
    def _soup_meanings(cls, html_tree: str)->List[str]:
        try:
            soup = BeautifulSoup(html_tree, 'html.parser')
            meaning_tags = soup.find(cls.TARGET_TAG, cls.TARGET_ATTR).find_all('span')
            cleaned_meaning = [valid_means for valid_means in meaning_tags \
                            if not 'class="cl"' in str(valid_means) if not 'class="etim"' in str(valid_means)]
            return list(dict.fromkeys([mean.get_text() for mean in cleaned_meaning]))
        except:
            return []