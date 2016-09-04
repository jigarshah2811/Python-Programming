'Collection of tools used in high frequency trading'

from __future__ import division
from my_validators import OneOf, String, Number

class PriceRange(object):

    kind = OneOf('stock', 'bond', 'option', 'currency', 'commodity')
    symbol = String(minsize=2, maxsize=5, predicate=str.isupper)
    low = Number(minvalue=0)
    high = Number(minvalue=0, maxvalue=100)

    def __init__(self, kind, symbol, low, high):
        self.kind = kind
        self.symbol = symbol
        self.low = low
        self.high = high

    @property
    def midpoint(self):
        return (self.low + self.high) / 2

##    @property
##    def kind(self):
##        return self._kind
##
##    @kind.setter
##    def kind(self, kind):
##        if kind not in {'stock', 'bond', 'option', 'currency', 'commodity'}:
##            raise ValueError('Not an allowed kind')
##        self._kind = kind

portfolio = [
    PriceRange('stock', 'CSCO', 26, 35),
    PriceRange('option', 'hp', 11, 45),
    PriceRange('stock', 'BOA', 32, 46),
    PriceRange('stock', 'WLP', 12.87, 34.15),
    PriceRange('option', 'WLP', -1.87, 14.15),
    PriceRange('option', 'BOA', 34j, 45),
    PriceRange('bond', 'HP', 62, 670),  
]
