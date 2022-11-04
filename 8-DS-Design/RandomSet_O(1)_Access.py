"""
https://leetcode.com/problems/insert-delete-getrandom-o1/description/
380. Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.
"""

from random import randint


class RandomizedSet(object):
    def __init__(self):
        self.d = {}
        self.l = []

    def insert(self, val):
        print(self.d)
        if val in self.d:
            return False

        # Insert val in list
        self.l.append(val)
        # Insert val in map {val: index}
        self.d[val] = len(self.l)-1
        print(self.d)
        return True

    def remove(self, val):
        if val not in self.d:
            return False

        lastVal = self.l[len(self.l)-1]
        self.d[lastVal] = self.d[val]
        self.l[self.d[val]] = lastVal

        # Remove last val
        self.l.pop()
        del self.d[lastVal]
        return True

    def getRandom(self):
        randomIndex = randint(0, len(self.l)-1)
        return self.l[randomIndex]

    def getList(self):
        return self.l


# Init an empty set
randomSet = RandomizedSet()

# Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);
print(randomSet.getList())

# Returns false as 2 does not exist in the set.
print(randomSet.remove(2));

# Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);
print(randomSet.getList())

# getRandom should return either 1 or 2 randomly.
print(randomSet.getRandom());

# Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);
print(randomSet.getList())

# 2 was already in the set, so return false.
print(randomSet.insert(2));
print(randomSet.getList())
print(randomSet.insert(2));
print(randomSet.getList())
print(randomSet.insert(2));
print(randomSet.getList())
# Since 2 is the only number in the set, getRandom always return 2.
print(randomSet.getRandom());
