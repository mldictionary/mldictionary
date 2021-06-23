# MLDictionary

## **MLDictionary** is word's dictionary for several language

```python
>>> from mldictionary import English
>>> english_dictionary = English()
>>> snake_means = english_dictionary.get_meanings('snake')
>>> len(snake_means)
4
>>> snake_means
'a reptile with a long body and no legs.'
...
```

<p align="center">
    <a href="https://pypi.org/project/mldictionary/" target="_blank" align="center">
        <img src="https://img.shields.io/pypi/v/mldictionary?color=%2334D058&label=pypi%20package" alt="Package version">
    </a>
</p>

---

## **Installing MLDictionary** 

```console
$ pip install mldictionary
```
MLDictionary officially supports 3.9+.

---

## Some examples

```python
>>> from mldictionary import Portuguese
>>> portuguese_dictionary = Portuguese()
>>> vida_means = portuguese_dictionary.get_meanings('vida')
>>> vida_means
['Conjunto dos hábitos e costumes de alguém; maneira de viver: tinha uma vida de milionário.']
...
>>> from mldictionary import Spanish
>>> spanish_dictionary = Spanish()
>>> yo_means = spanish_dictionary.get_meanings('yo')
>>> yo_means
['pron. Forma del pron. pers. com. de primera persona singular,' ...]
```

---

### Make your own dictionary
```python
import re # to take html tags out with regex
from typing import List, Union

from mldictionary import Dictionary

class MyOwnDictionary(Dictionary):
    URL = 'somedictionary.com' #required
    XPATH = '//xpath//of[@class="means"]' #required
    LANGUAGE = 'language name' #requerid

    @classmethod
    def _clean_html(cls, meanings_html: List[str])->Union[str, bool]:
       '''
        method to take html tags out, for some examples, access:
        https://github.com/PabloEmidio/mldictionary/tree/main/mldictionary 
       '''
>>> myowndictionary = MyOwnDictionary()
>>> myowndictionary.get_meanings('other language word')
```