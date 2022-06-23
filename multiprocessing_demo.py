''' Demonstrate how to use multi-processing to speed-up I/O bound applications
    such as those commonly found in networking applications.

    Learn to group tasks into parallelizable work (making roads or vacuuming)
    versus non-parallelizable work that requires sequential step (making babies).

    Three pitfalls of thin channel communication:
    1) Too many trips back and forth
    2) Not doing enough work relative to the travel time
    3) Taking too much with you or bringing too much back

RR1:  Get your app tested and debugged in a singled process mode first
      before you start threading.  Multiprocessing NEVER makes debugging easier.

RR2:  Use caution when multiprocessing or forking from with an IDE.
      Watch-out, you might end-up forking your IDE as well.

GIL:  Global interpreter lock.   CPython has lots of global states.
      There is a lock head whenever that state can be updated
      which is most of the time.  Because of this, multithread code
      in CPython runs as many threads your want but only ONE executes
      at a time.  This means CPython threads are great for IO bound
      and a disaster for CPU bound.

Q. How big should the pool be for multiple processes?
A. Could set it to the number of cores.
   If any processes block, you're better of with more than the number of cores.

How to partition strings into equal length segments:
    >>> s = 'she sells sea shells by the sea shore and peter piper picked a peck of pickled peppers'
    >>> cores = 4
    >>> segment = -(-len(s) // 4)
    >>> segments = [s[i*segment: i*segment+segment] for i in range(cores)]
    >>> sum(pool.imap(lambda s: s.count('e'), segments))       # <-- Don't do this because you're passing in too much data
    >>> sum(map(lambda i: s[i*segment:i*segment+segment].count('e'), range(cores)))  # <-- better to only pass in the segment number

When segmenting data, some care needs to be taken for data at the split boundaries:

    >>> def count_words(s):
            return len(re.findall(r'\w+', s))

    >>> count_words(s)
    17
    >>> sum(map(count_words, segments))
    20
    >>> for seg in segments:
            print count_words(seg), seg
            
    5 she sells sea shells b
    6 y the sea shore and pe
    5 ter piper picked a pec
    4 k of pickled peppers
'''

import urllib
from pprint import pprint
from itertools import imap

THREADED_VERSION = True     # Making False will go multi-processing Pool, & optimize IO get_site()

if THREADED_VERSION:
    from multiprocessing.pool import ThreadPool as Pool
else:
    from multiprocessing.pool import Pool

sites = [
    'http://www.cnn.com',
    # 'http://www.python.org',
    'http://www.jython.org',
    'http://www.pypy.org',
    #'http://www.perl.org',
    'http://www.cisco.com',
    #'http://www.facebook.com',
    #'http://www.twitter.com',
    'http://www.macrumors.com/',
    'http://arstechnica.com/',
    'http://www.reuters.com/',
    'http://abcnews.go.com/',
    'http://www.cnbc.com/',
    'http://www.cnbc.com/',
    #'http://www.yahoo.com/',
]


def get_site(site):
    '''
        1 DNS lookup UDP Request                                10
        2 DNS UDP response                                      500
        1 Acquire a TCP socket from OS                          5       <-- Parallizable but not worth it
        3 TCP Connection (SYN, ACK, SYN/ACK)
        4 Send an HTTP GET Request
        5 || Receive packets back and save them in memory       I/O
        5    Group all the packets into a single string         CPU     <-- Parallizable but not worth it
        7 Return the string

   '''

    print 'Fetching', site
    u = urllib.urlopen(site)

    '''
                Program
                    |
                    /   \
                Thread  Processes
                |           |
                / \         \
            page    len         len (BEST due to IO operation is multiproceesing now)
    '''
    # Returning entire website
    # return site, u.read()

    # Optimized?? Returning only len... NO because This is multithreading, it's already shared 
    return site, len(u.read())


def mymap(func, iterable):
    return [func(x) for x in iterable]


# Everything shared should be done before Pool() to use COW (copy on write)
pool = Pool(20)
pprint(zip(sites, imap(len, imap(get_site, sites))))

for site, size in pool.imap_unorderd(get_site, sites): # imap_unordered generates a generator
    print size, site
