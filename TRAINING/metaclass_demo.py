
'''
                 Metaclass                                  __call__ 
                 ^ 
                / behavior controlled by
               /                                            Soldier(a)
             Class --> attributes unique to each instance   __call__           <-- type
             ^ 
            / behavior controlled by
           /
Instance  o--> attributes unique to each instance            s(a)              <-- object
'''

## The Regular Way to Make a soldier class #######################################################

class Soldier(object):
    'The very model of a modern major general'

    def __new__(cls, *args):                               # Create a new instance (give it a __class__ and empty __dict__)
        # Make an instance
        # that has inst.__class__ = cls
        # and has  inst.__dict__ = {}
        print 'Making a new instance', cls
        return object.__new__(cls, *args)

    def __init__(self, rank, lastname):                    # Initialize an instance (put data in the __dict__)
        print 'Initializing a new soldier instance'
        self.rank = rank
        self.lastname = lastname

    def __getattr__(self, command):                        # Controls what the dot does
        print "I don't know how to %r" % command

    def __call__(self, phrase):                            # Controls what the parentheses do
        print phrase, 'back!'

    def __repr__(self):                                    # Controls the appearance of the object
        return '%s(rank=%r, lastname=%r)' % (self.__class__.__name__, self.rank, self.lastname)

    def run(self):                                         # Non-dunder names add other custom behaviors
        print 'The %s is running' % self.rank

    def shoot(self):
        print '%s %s is shooting' % (self.rank, self.lastname)

s = Soldier('Captain', 'America')
t = Soldier('General', 'Nuisance')
u = Soldier('Cadet', 'Battle')
print s
t.run()
u.shoot()
s('Hey you')
t.surrender

##############################################

class CuteReprMeta(type):
    def __repr__(cls):
        return '<<Class %r>>' % cls.__name__

class Soldier2(object):
    'The very model of a modern major general'

    __metaclass__ = CuteReprMeta

    def __new__(cls, *args):                               # Create a new instance (give it a __class__ and empty __dict__)
        # Make an instance
        # that has inst.__class__ = cls
        # and has  inst.__dict__ = {}
        print 'Making a new instance', cls
        return object.__new__(cls, *args)

    def __init__(self, rank, lastname):                    # Initialize an instance (put data in the __dict__)
        print 'Initializing a new soldier instance'
        self.rank = rank
        self.lastname = lastname

    def __repr__(self):                                    # Controls the appearance of the object
        return '%s(rank=%r, lastname=%r)' % (self.__class__.__name__, self.rank, self.lastname)

    def run(self):                                         # Non-dunder names add other custom behaviors
        print 'The %s is running' % self.rank

#### Instance Tracking #####################

instances = set()

class InstanceTrackingMeta(type):
    def __call__(cls, *args):
        inst = type.__call__(cls, *args)
        instances.add(inst)
        return inst

class Soldier3(object):
    'The very model of a modern major general'

    __metaclass__ = InstanceTrackingMeta

    def __new__(cls, *args):                               # Create a new instance (give it a __class__ and empty __dict__)
        # Make an instance
        # that has inst.__class__ = cls
        # and has  inst.__dict__ = {}
        print 'Making a new instance', cls
        return object.__new__(cls, *args)

    def __init__(self, rank, lastname):                    # Initialize an instance (put data in the __dict__)
        print 'Initializing a new soldier instance'
        self.rank = rank
        self.lastname = lastname

    def __repr__(self):                                    # Controls the appearance of the object
        return '%s(rank=%r, lastname=%r)' % (self.__class__.__name__, self.rank, self.lastname)

    def run(self):                                         # Non-dunder names add other custom behaviors
        print 'The %s is running' % self.rank

#### Singleton #####################

singletons = dict()

class SingletonMeta(type):
    def __call__(cls, *args):
        uid = (cls.__name__, args)
        if uid in singletons:
            return singletons[uid]
        inst = type.__call__(cls, *args)
        singletons[uid] = inst
        return inst

class Soldier4(object):
    'The very model of a modern major general'

    __metaclass__ = SingletonMeta

    def __new__(cls, *args):                               # Create a new instance (give it a __class__ and empty __dict__)
        # Make an instance
        # that has inst.__class__ = cls
        # and has  inst.__dict__ = {}
        print 'Making a new instance', cls
        return object.__new__(cls, *args)

    def __init__(self, rank, lastname):                    # Initialize an instance (put data in the __dict__)
        print 'Initializing a new soldier instance'
        self.rank = rank
        self.lastname = lastname

    def __repr__(self):                                    # Controls the appearance of the object
        return '%s(rank=%r, lastname=%r)' % (self.__class__.__name__, self.rank, self.lastname)

    def run(self):                                         # Non-dunder names add other custom behaviors
        print 'The %s is running' % self.rank

#### Dynamic Attribute #####################

import time

class DynamicAttributeMeta(type):
    def __getattribute__(cls, attr):
        if attr == 'now':
            return time.ctime()
        return type.__getattribute__(cls, attr)
    
class Soldier5(object):
    'The very model of a modern major general'

    __metaclass__ = DynamicAttributeMeta

    x = 10

    def __new__(cls, *args):                               # Create a new instance (give it a __class__ and empty __dict__)
        # Make an instance
        # that has inst.__class__ = cls
        # and has  inst.__dict__ = {}
        print 'Making a new instance', cls
        return object.__new__(cls, *args)

    def __init__(self, rank, lastname):                    # Initialize an instance (put data in the __dict__)
        print 'Initializing a new soldier instance'
        self.rank = rank
        self.lastname = lastname

    def __repr__(self):                                    # Controls the appearance of the object
        return '%s(rank=%r, lastname=%r)' % (self.__class__.__name__, self.rank, self.lastname)

    def run(self):                                         # Non-dunder names add other custom behaviors
        print 'The %s is running' % self.rank

#### Add Extra Attributes #####################

class TimestampMeta(type):
    def __new__(mcls, name, bases, mapping):
        mapping['creation_time'] = time.ctime()
        return type.__new__(mcls, name, bases, mapping)

class Soldier6(object):
    'The very model of a modern major general'

    __metaclass__ = TimestampMeta

    x = 10

    def __new__(cls, *args):                               # Create a new instance (give it a __class__ and empty __dict__)
        # Make an instance
        # that has inst.__class__ = cls
        # and has  inst.__dict__ = {}
        print 'Making a new instance', cls
        return object.__new__(cls, *args)

    def __init__(self, rank, lastname):                    # Initialize an instance (put data in the __dict__)
        print 'Initializing a new soldier instance'
        self.rank = rank
        self.lastname = lastname

    def __repr__(self):                                    # Controls the appearance of the object
        return '%s(rank=%r, lastname=%r)' % (self.__class__.__name__, self.rank, self.lastname)

    def run(self):                                         # Non-dunder names add other custom behaviors
        print 'The %s is running' % self.rank
    

