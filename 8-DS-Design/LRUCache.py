"""
https://www.kunxi.org/blog/2014/05/lru-cache-in-python/
https://leetcode.com/problems/lru-cache/solution/
"""

import collections

"""
Using UnOrdered Map (Dictionary)
"""
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.mostRecent = 0     # Marker for most recent get/put entry that keeps higher number to keep cache for last entry, refreshed
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.mostRecent
            self.mostRecent += 1
            return self.cache[key]
        return -1

    def set(self, key, value):
        if len(self.cache) > self.capacity:
            # Find the LRU entry to purge       # mostRecent = min number
            old_key = min(self.lru.keys(), key=self.mostRecentKey)
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.mostRecent
        self.mostRecent += 1
    
    def mostRecentKey(self, k):
        return self.lru[k]

"""
Using Ordered Dict
MostRecent is always on the top
LeastRecent is always in the bottom
"""
class LRUCacheOptimized:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)     # Pop and Push this value to make it MostRecent
            self.cache[key] = value
            print("get returns", value)
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)         # Key exists, Update
        except KeyError:
            if len(self.cache) >= self.capacity:    # Full
                print("purge")
                self.cache.popitem(last=False)      # Purge old entry (LeastRecent is always in the bottom)
        print("set sets", value)
        self.cache[key] = value                     # set New entry



# lru = LRUCacheOptimized(2)
# print(list(filter(lambda x: x, [lru.set(1, 1),lru.set(2, 2),lru.set(1, 1), lru.set(3, 3),lru.get(3), lru.get(1)])))

"""
Approach 2: Hashmap + DeQue (Doubly Linked-List)
LRU HashMap ---> {key, DequeueIndex}        Index in Dequeue where the value for this key is: For O(1) access
Dequeue: Front Least Recent entry. Back will be Most recent entry
"""


class Solution:
    def __init__(self, capacity=10):
        self.q = collections.deque()
        self.cache = collections.defaultdict()
        self.capacity = capacity

    def get(self, key):
        try:
            index = self.cache[key]
        except KeyError:
            return -1

        print("Get start: ", self.q)
        value = self.q[index]  # Get it from in-between
        del self.q[index]  # Remove old entry
        self.q.append(value)  # Make it most recent
        self.cache[key] = len(self.q)-1
        print("Get end: ", self.q)

        return value

    def set(self, key, val):
        print("Set start: ", self.q)
        if key in self.cache:
            index = self.cache[key]  # Key exists, so update

            del self.q[index]  # Remove old entry
            self.q.append(val)  # Create new entry
            self.cache[key] = len(self.q) - 1  # Update LRU Location to this index

        else: # Key doesn't already exists, New Key
            if len(self.q) >= self.capacity:
                old_key = self.q[0]
                del self.cache[old_key]
                self.q.popleft()                # Purge most recent entry from front of Queue

            self.q.append(val)  # Create new entry
            self.cache[key] = len(self.q) - 1  # Update LRU Location to this index

        print("Set end: ", self.q)

lru = Solution(2)
print(list(filter(lambda x: x, [lru.set(1, 1),lru.set(2, 2), lru.set(3, 3), lru.get(1), lru.get(2), lru.get(3)])))
