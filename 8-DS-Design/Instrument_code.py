''' Goals:
* Learn to instrumented Python for performance analysis
* Practice subclassing builtin types
* Review the dunder methods
* Solidify knowledge of how containers work
* Learn to use bisection
'''

from bisect import bisect


def reset():
    global cmpcnt, hashcnt
    cmpcnt = 0
    hashcnt = 0


def show():
    print('%d comparisons and %d hashes' % (cmpcnt, hashcnt))


class Int(int):
    'Instrumented tracer version of int'

    def __cmp__(self, other):
        global cmpcnt
        cmpcnt += 1
        print('Comparing %r to %r' % (self, other))
        return int.__cmp__(self, other)

    def __hash__(self):
        global hashcnt
        hashcnt += 1
        print('hashing %r' % self)
        return int.__hash__(self)

# Study list searches ######################################################

s = list(map(Int, [10, 20, 30, 50, 20, 5, 10, 15, 20]))
a = Int(111)
b = Int(20)
c = s[2]

reset(); print(a in s); show()        # Linear search, from left-to-right. When there is no match, we take len(s) comparisons
reset(); print(b in s); show()        # Linear search has an early-out for a match.
reset(); print(c in s); show()        # Identify implies equality, saving one test.

reset(); s.sort() ; show()           # O(n log n) in the worst case, but Timsort can often approach O(n)
reset(); print(bisect(s, a)); show()  # O(log n)
reset(); print(bisect(s, b)); show()  # Bisect provides consistent lookup behavior into data ranges
reset(); print(bisect(s, c)); show()  # Total cost for k lookups in n items = k log n + n log n

# Study set searches #######################################################

data = list(map(Int, [10, 20, 30, 50, 20, 5, 10, 15, 20]))
a = Int(111)
b = Int(20)
c = data[2]

odata = list(map(Int, [10, 20, 30, 50, 20, 5, 10, 15, 20]))
u = set(odata)

reset(); s = set(data); show()       # Cost of building a set is n hashes and one compare for each duplicate
reset(); print(a in s); show()        # Cost of missed set lookup is 1 hash and 0 compares
reset(); print(b in s); show()        # Cost of succesful set lookup is 1 hash and 1 compare
reset(); print(c in s); show()        # Cost of succesful set identiy lookup is 1 hash and 0 compare

reset(); print(s & u); show()         # Cost of intersection/union/difference: 0 hashes and 1 comparision
reset(); print(s | u); show()
reset(); print(s - u); show()

reset(); print(dict.fromkeys(s))     # No cost to convert in a dict
