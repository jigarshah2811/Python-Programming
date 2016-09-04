'Learn exactly how "import" works and how to customize it'

import os
import sys
import urllib

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


def myimport(modname):
    if modname in modules:
        globals()[modname] = modules[modname]
        return
    
    filename = modname + '.py'

    if filename.startswith('http://'):
        print 'Starting modname:', modname
        
        u = urllib.urlopen(filename)
        code = u.read()
        u.close()
        fullname = filename
        modname = os.path.split(modname)[1]

        print 'Code:', code
        print 'Fullname:', fullname
        print 'Modname:', modname
        
    else:
        for dirname in sys.path:
            # PYC file:  (magic_number: version_of_python, timestamp, marshal.dumps(code))
            fullname = os.path.join(dirname, filename)
            try:    
                with open(fullname) as f:
                    code = f.read()
                break
            except IOError:
                pass
        else:
            raise ImportError('Cannot find %r on sys.path' % modname)
        
    namespace = {}
    namespace['__name__'] = modname
    namespace['__file__'] = fullname
    namespace['__package__'] = None
    exec code in namespace

    module = Module(namespace)
    globals()[modname] = module
    modules[modname] = module

def myreload(module):
    modname = module.__name__
    del modules[modname]
    myimport(modname)
    return modules[modname]

if __name__ == '__main__':
    myimport('sample')
    print sample.n
    print sample.cube(12)

    myimport('random')
    print random.randrange(10000)

    myimport('http://users.rcn.com/python/download/puzzle')
