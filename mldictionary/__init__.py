"""MLDictionary library, for all of us who want to know word's meanings."""

__author__ = 'Pablo Emidio'
__email__ = 'p.emidiodev@gmail.com'
__version__ = '0.2.6'

import logging

from .dictionary import Dictionary
from .english import English
from .portuguese import Portuguese
from .spanish import Spanish


logging.basicConfig(
   level=logging.INFO,
   format='%(asctime)s - %(module)s - %(message)s'
)
