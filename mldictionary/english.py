from .dictionary import Dictionary

class English(Dictionary):
    URL = 'https://dictionary.cambridge.org/us/dictionary/english/{}'
    TARGET_TAG = 'div'
    TARGET_ATTR = {'class': 'ddef_d'}
    LANGUAGE = 'English'
