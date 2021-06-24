from .dictionary import Dictionary

class Spanish(Dictionary):
    URL = 'https://dle.rae.es/{}?m=form'
    TARGET_TAG = 'p'
    TARGET_ATTR = {'class': 'j'}
    LANGUAGE = 'Spanish'
