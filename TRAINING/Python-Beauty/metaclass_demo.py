
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

##################################### MY METACLASS ######################################
class CuteMeta(type):
    def __repr__(cls):
        return '<<Class %r>>' % cls.__name__


## The Regular Way to Make a soldier class #######################################################

class Soldier(object):
    'The very model of a modern major general'

    __metaclass__ = CuteMeta
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
#t.surrender

####### Instance Tracking #########

instances = set()

####### Dynamic attribute #####

import time

class DynamicAttributeMeta(type):
    def __getattribute__(cls, attr):
        if attr =='now':
            print "Changing behavior...."
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

###### Multiple MetaClasses #####

class CombinedMeta(DynamicAttributeMeta, CuteMeta):
    def __init__(cls):
        pass


#### ADD Extra Attribute #####

class TimeStampMeta(type):
    def __new__(mcls, name, bases, mapping): # why mcls instead of cls, cause it's '__new__'!
        mapping['creation_time'] = time.ctime()
        return type.__new__(mcls, name, bases, mapping)

class Soldier6(object):
    'The very model of a modern major general'

    __metaclass__ = TimeStampMeta

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

class SuperSoldier(Soldier6):
    pass
