'Learn exactly how "import" works and how to customize it'

from pprint import pprint
import sys
import os

# Caching
modules = {}
    
class Module(object):

    def __init__(self, namespace):
        object.__setattr__(self, 'namespace', namespace)

    def __getattr__(self, attr):
        try:
            return self.namespace[attr]
        except KeyError:
            raise AttributeError(attr)
    
    def __setattr__(self, attr, value):
        self.namespace[attr] = value

    def __delattr__(self, attr):
        try:
            del self.namespace[attr]
        except KeyError:
            raise AttributeError(attr)

    def __dir__(self):
        return sorted(self.namespace.keys())

    def __repr__(self):
        return '<Module %r from %r>' % (self.__name__, self.__file__)

def myreload(module):
    modname = module.__name__
    del modules[modname]
    myimport(modname)
    modules[modname] = module

def myimport(modname):

    # Caching
    if modname in modules:
        # Bypass exec completely
        globals()[modname] = modules[modname]
        return
        
    filename = modname + '.py'
    for dirname in sys.path:
        # PYC File
        fullname = os.path.join(dirname, filename)
        print 'Looking for', fullname
        try:
            with open(fullname) as f:
                code = f.read()
            print 'Found'
            break
        except IOError:
            print 'No luck'
            pass
    else:
        raise ImportError("Can not find the module %r" % fullname)
        
    namespace = {}
    namespace['__name__'] = modname
    namespace['__file__'] = fullname
    namespace['__package__'] = None
    exec code in namespace
    module = Module(namespace)
    globals()[modname] = module
    modules[modname] = module

if __name__ == "__main__":
    myimport('sample')
    print sample.n
    print sample.cube(12)

    myimport('random')
    print random.randrange(10000)
    myimport('http://users.rcn.com/python/download/puzzle')
