class Descr(object):

    # Gets self=instance of itself + obj (gets instance of A also)
    def __get__(self, obj, objtype): 
        print "Invocation!"
        print "Returning x+10"
        return obj.x+10


class GoodUser(object):    # Class has to inherit from object for descriptor to work

    def __init__(self, x):
        self.x = x

    plus_ten = Descr()

class BadUser(object):
    
    def __init__(self, x):
        self.x = x
        self.plus_ten = Descr()
