from pprint import pprint
from DS_bloom_filter_optimized import BloomFilter
import re

try:
    import cPickle as pickle
except ImportError:
    import pickle


def make_checker():
    print ("Creating a pickle of BloomFilter")
    with open('notes3/words.txt') as f:
        words = f.read().lower().split()

    bfCaching = BloomFilter(words, population=4000000, probe=10)

    with open('words.pcl', 'wb') as f:
        pickle.dump(bfCaching, f)

    # print "abacinatinn" in bfCaching    # Now we can check if word is in dictionary
    return True


def spell_check(text):
    """
    Let's optimize this"
    IO Operations using Pickle
    """
    try:
        with open('words.pcl', 'rb') as f:
            print 'Reading pickle - words.pcl'
            checker = pickle.load(f)
    except IOError:
        raise IOError("Pickle {0} is not created".format('words.pcl'))

    """ Get all words to check against dict """
    words = re.findall(r"[a-z\'\-]+", text.lower())

    print 'Spell check on words:'
    print '-----------'
    print words

    print 'Misspelled:'
    print '-----------'
    for word in words:
        if word not in checker:
            print word

if __name__ == '__main__':
    known_words = '''
        a aid all an army assistance bad be
        beautiful by child children come country
        flag for from go going good help is later
        man many men my no now of our some state
        the their to ugly was with woman women
    '''

    text = '''
            Now, iss the tymme for all
            guhd men tooo comee to the
            ayd of thur country and city.
    '''

    make_checker()
    spell_check(text)
