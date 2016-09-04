THREADED_VERSION = False

if THREADED_VERSION:
    from multiprocessing.pool import ThreadPool
else:
    from multiprocessing.pool import Pool

from itertools import imap

# BOTTLENACK: Doing too little work for a process (At paris)
def square(x):
    return x * x


def sum_of_square((low, high)):
    return sum(x * x for x in xrange(low, high))


n = 100000000
cores = 4
threadPerCore = 2
coresize = n // cores


# print sum(map(square, range(n)))        # 640 MB
# Optimized (imap)
# print sum(imap(square, range(n)))        # 300 bytes

mp = Pool(cores)
# mt = ThreadPool(threadPerCore)

ranges = [(i*coresize, (i+1)*coresize) for i in range(cores)]

# print sum(mp.imap_unordered(square, xrange(n)))
print sum(mp.imap(sum_of_square, ranges))
