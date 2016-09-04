class CIDict(dict):
    'Create a case-insensitve dictionary'

    def __getitem__(self, key):                             # d[key]
        key = key.lower()
        return dict.__getitem__(self, key)

    def __missing__(self, key):                             # called by dict.__getitem__ when a key is missing
        raise KeyError('Missing key, could be any case variant of %r' % key)        

    def __setitem__(self, key, value):                      # d[key] = value
        key = key.lower()
        return dict.__setitem__(self, key, value)

    def __delitem__(self, key):                             # del d[key]
        key = key.lower()
        return dict.__delitem__(self, key)

d = CIDict()
d['RAYMOND'] = 'red'
print d['RAYmond']

class ZeroDict(dict):
    def __missing__(self, key):
        return 0

d = ZeroDict()
for color in 'red green red blue red green'.split():
    d[color] += 1
print d

class CDot(object):

    def __getattribute__(self, attr):                       # c.x           getattr(c, 'x')
        print 'Looking up: %r' % attr
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):                            # called by object.__getattribute__ when an attribute is missing
        print 'Oh no, %r is missing' % attr
        raise AttributeError('Oops, I did it again')

    def __setattr__(self, attr, value):                     # c.x = 10      setattr(c, 'x', 10)
        print 'Setting %r to %r' % (attr, value)
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):                            # del c.x       delattr(c, 'x')
        print 'Deleting: %r' % attr
        return object.__delattr__(self, attr)    

c = CDot()

class CIDot(object):
    'Case insensitive attribute lookup'

    def __getattribute__(self, attr):                       # c.x           getattr(c, 'x')
        attr = attr.lower()
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):                            # called by object.__getattribute__ when an attribute is missing
        raise AttributeError('Could be any variant of %r' % attr)

    def __setattr__(self, attr, value):                     # c.x = 10      setattr(c, 'x', 10)
        attr = attr.lower()
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):                            # del c.x       delattr(c, 'x')
        attr = attr.lower()
        return object.__delattr__(self, attr)    

c = CIDot()
c.X = 10
print c.x
