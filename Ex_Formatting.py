"""
User .format() for all string formatting in python
"""
# print 'today is {new} and yesterday was {old}'.format(new=10, old=20)

from datetime import *

class IPAddr(object):
    def __init__(self, *octets):
        self.octets = octets

    def __repr__(self):
        # return '%s%r' % (self.__class__.__name__, self.octets)
        return '{0.__class__.__name__}{0.octets}'.format(self, self.octets)

    def __format__(self, fmt):
        if fmt == 'x':
            return '.'.join([format(o, '02x') for o in self.octets])
        elif fmt == '':
            return '.'.join(map(str, self.octets))
        else:
            raise ValueError('Unknown format code: %r, Use x or nothing', fmt)
        #return fmt

n = datetime.now()
print format(n, 'Today is {%a}')

a = IPAddr(192, 168, 10, 1)
print a.octets
print 'The iP Address is {0}'.format(a)
print 'The iP Address is {0:x}'.format(a)
