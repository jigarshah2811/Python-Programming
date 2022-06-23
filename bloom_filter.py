"""
Space efficient probablistic DS for membership testing
Google uses it before Map Reduce
"""

from random import seed, sample

class BloomFilter(object):

    def __init__(self, iterable=(), population=56, probes=6):
        self.population = xrange(population)
        self.probes = probes
        self.data = set()
        for name in iterable:
            self.add(name)

    def add(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        print lucky
        self.data.update(lucky)

    def __contains__(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        return set(lucky).issubset(self.data)
        #return set(lucky) <= self.data

if __name__ == "__main__":

    names = 'raymond rachel matthew ramon gayle dennis sharon'
    hettingers = BloomFilter(names, 100, 10)
    for name in names.split():
        hettingers.add(name)
    print 'rachel' in hettingers
    print 'Jigar' in hettingers
