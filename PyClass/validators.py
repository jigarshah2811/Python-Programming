'Create a high quality module of reusable and extendable data validators'

class Validator(object):

    counter = 0

    def __init__(self):
        self.private_name = '_%s_%d' % (self.__class__.__name__, Validator.counter)
        Validator.counter += 1

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    def validate(self, value):
        pass

class OneOf(Validator):

    def __init__(self, *options):
        Validator.__init__(self)
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError('%r not a valid option.  should be one of: %r' % (value, self.options))

class String(Validator):

    def __init__(self, minsize=0, maxsize=None, predicate=None):
        Validator.__init__(self)
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a str')
        if len(value) < self.minsize:
            raise ValueError('String is too short, must be at least %d long' % self.minsize)
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError('String is too long, must be no bigger than %d long' % self.maxsize)
        if self.predicate is not None and not self.predicate(value):
            raise ValueError('Expected true from %r' % self.predicate)

class Number(Validator):

    def __init__(self, minvalue=None, maxvalue=None):
        Validator.__init__(self)
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('Expected an int or float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError('%r is too small.  Must be at least %r.' % (value, self.minvalue))
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError('%r is too big.  Must be no more than %r.' % (value, self.maxvalue))        
                             
