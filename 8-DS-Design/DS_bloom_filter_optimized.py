"""
https://en.wikipedia.org/wiki/Bloom_filter
"""
from random import seed, sample


class BloomFilter(object):

    def __init__(self, iterable=(), population=10, probe=2):
        self.population = range(population)
        self.probe = probe
        self.data = bytearray(population)
        for name in iterable:
            self.add(name)

    def add(self, name):
        seed(name)
        lucky = sample(self.population, self.probe)
        for i in lucky:
            self.data[i] = 1

    def __contains__(self, name):
        seed(name)
        lucky = sample(self.population, self.probe)
        return all(self.data[i] for i in lucky)


def main():
    names = "Jigar Krups Pilu Nency Papa Mummy"
    shahFamily = BloomFilter(names.split(), 100, 10)
    print('Jigar' in shahFamily)
    print('nobody' in shahFamily)

if __name__ == "__main__":
    main()
