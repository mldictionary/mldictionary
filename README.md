# MLDictionary

## **MLDictionary** is word's dictionary for several language

```python
>>> from mldictionary import English
>>> english_dictionary = English()
>>> snake_means = english_dictionary.get_meanings('snake')
>>> len(snake_means)
4
>>> snake_means
['a reptile with a long body and no legs: ' ...]
...
```

<p align="center">
    <a href="https://pypi.org/project/mldictionary/" target="_blank" align="center">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/mldictionary?color=%233f7&logo=pypi&style=plastic">    
    </a>&nbsp;&nbsp;
    <a href="https://pypi.org/project/mldictionary/" target="_blank" align="center">
        <img alt="PyPI - License" src="https://img.shields.io/pypi/l/mldictionary?color=%237f7&logo=pypi&style=plastic">    
    </a>&nbsp;&nbsp;
    <a href="https://pypi.org/project/mldictionary/" target="_blank" align="center">
<img alt="GitHub Workflow Status (event)" src="https://img.shields.io/github/workflow/status/pabloemidio/mldictionary/unittest?color=%233f7&label=tests&logo=pypi&style=plastic">
    </a>&nbsp;&nbsp;
    <a href="https://pypi.org/project/mldictionary/" target="_blank" align="center">
        <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/mldictionary?color=%237f7&logo=pypi&style=plastic">    
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
['Conjunto dos hábitos e costumes de alguém; maneira de viver: tinha uma vida de milionário.' ...]
>>> from mldictionary import Spanish
>>> spanish_dictionary = Spanish()
>>> coche_means = spanish_dictionary.get_meanings('coche')
>>> coche_means
['Automóvil destinado al transporte de personas y con capacidad no superior a siete plazas.' ...]
```

---

### Make your own dictionary
```python
from mldictionary import Dictionary

class MyOwnDictionary(Dictionary):
    url = 'somedictionary.com'
    language = 'language name'
    target_tag = 'tag_where_means_is'
    target_attr = {'attr': 'attr_value'}
    replaces = {'something', 'another thing'}

>>> myowndictionary = MyOwnDictionary()
>>> myowndictionary.get_meanings('other language word')
```
To more details, see the [wiki](https://github.com/PabloEmidio/mldictionary/wiki)

Also, it has a insightful [article on linkedin](https://www.linkedin.com/pulse/mldictionary-pablo-em%25C3%25ADdio)
