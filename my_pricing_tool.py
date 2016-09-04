'Collection of tools used in high frequency trading'

from __future__ import division
from my_validators import OneOf

class PriceRange(object):

    
    kind = OneOf('stock', 'bond', 'option', 'currency', 'commodity')
    #symbol = String(minsize=2, maxsize=5, predicate=str.isupper)
    #low = Number(minvalue=0)
    #high = Number(minvalue=0, maxvalue=100)
     
    def __init__(self, kind, symbol, low, high):
        self.kind = kind
        self.symbol = symbol
        self.low = low
        #What are the problems?? floating needs __future__
        # also works only during __init__ so dynamically change low high won't change midpoint
        # self.midpoint = (low + high) / 2  
        self.high =high

    @property   # Transforms attribute access to method access
    def midpoint(self):
        return (self.low + self.high) / 2

    @property
    def kind(self):
        return self._kind

    @kind.setter
    def kind(self, kind):
        if kind not in {'stock', 'bond', 'option', 'currency', 'commodity'}:
            raise ValueError('Not allowed kind')
        self._kind = kind

portfolio = [
    PriceRange('Stock', 'CSCO', 26, 35),
    PriceRange('bond', 'hp', 11, 45),
    PriceRange('Stock', 'BOA', 32, 46),
    PriceRange('stock', 'WLP', 12.87, 34.15),
    PriceRange('option', 'WLP', -1.87, 14.15),
    PriceRange('option', 'BOA', 34j, 45),
    PriceRange('bond', 'BOA', 62, 670),  
]
