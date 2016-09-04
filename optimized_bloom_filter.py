"""
Space efficient probablistic DS for membership testing
Google uses it before Map Reduce
"""

from random import seed, sample


class BloomFilter1(object):

    def __init__(self, iterable=(), population=56, probes=6):
        self.population = xrange(population)
        self.probes = probes

        # self.data = list()                # Efficient compare to set() in terms of size, list refs points to 0s and 1s
        # self.data = bytearray(population)   # Efficient compare to list() in terms of size
        self.data = bytearray(population)   # Efficient compare to list() in terms of size

        for name in iterable:
            self.add(name)

    def add(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        for n in lucky:
            self.data[n] = 1

    def __contains__(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        return all(self.data[i] for i in lucky)

if __name__ == "__main__":

    names = 'raymond rachel matthew ramon gayle dennis sharon'
    hettingers = BloomFilter(names.split(), 100, 10)
    print 'rachel' in hettingers
    print 'Jigar' in hettingers
