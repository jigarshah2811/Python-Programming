'Space-efficient probabalistic data structure for membership testing'

# https://en.wikipedia.org/wiki/Bloom_filter

from random import seed, sample
try:
    from cbitarray import BitArray
except:
    from bitarray import BitArray

class BloomFilter(object):

    def __init__(self, iterable=(), population=56, probes=6):
        self.population = xrange(population)
        self.probes = probes
        self.data = BitArray(population)
        for name in iterable:
            self.add(name)

    def add(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        for i in lucky:
            self.data[i] = 1

    def __contains__(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        return all(self.data[i] for i in lucky)

if __name__ == '__main__':

    hettingers = BloomFilter('raymond rachel matthew ramon gayle dennis sharon'.split())
    print 'rachel' in hettingers
    print 'monica' in hettingers
