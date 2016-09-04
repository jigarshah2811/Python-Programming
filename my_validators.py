'Collection of tools used in high frequency trading'

from __future__ import division


class Validator(object):

    counter = 0

    def __init__(self):
        self.private_name = '_%s_%d' % (self.__class__.__name__, counter)
        Validator.counter += 1

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)
        

class OneOf(Validator):
    
    def __init__(self, *options):
        Validator.__init__(self)
        self.options = set(options) # set because O(1) lookup


    def validate(self, value):
        if value not in self.options:
            raise ValueError("%r not a valid option. Should be one of: %r" % (value, self.options))
        
        
class String(Validator):
    
    def __init__(self, minsize=0, maxsize=None, predicate=None):
        Validator.__init__(self)
        self.options = set(options) # set because O(1) lookup
            
    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Expecting a str")
        if len(value) < self.minsize:
            raise ValueError("String too short, must be at least %d long" % self.minsize)
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError("String too long, must be at max %d long" % self.maxsize)
        if self.predicate is not None and not self.predicate(value):
            raise ValueError("Expected true from %r" % self.predicate)
        
class Number(object):

    counter = 0
    
    def __init__(self, minValue=None, maxValue=None):
        Validator.__init__(self)
        self.minValue = minValue
        self.maxValue = maxValue


    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Expecting an int or float")
        if self.minValue is not None and value < self.minValue:
            raise ValueError("%d is too small. Must be at least %d long", self.minValue)
        if self.maxValue is not None and value > self.maxValue:
            raise ValueError("%d is too big. Must be at most %d long", self.maxValue)
    
        
        
