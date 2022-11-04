"""
https://leetcode.com/problems/design-hashmap/discuss/185347/Hash-with-Chaining-Python
"""


class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class HashMap:
    def __init__(self):
        """
        Initialize DS here: A HashMap is List of 1000 nodes, Each Index in List can have chain (ListNodes)
        """
        self.capacity = 1000
        self.m = [None] * self.capacity

    def put(self, key, value):
        """
        Key will always be in range (0...1million) and value can be any int
        :param key: int
        :param value: int
        :return: void
        """
        index = key % self.capacity

        if self.m[index] is None:   # No pair(key,val) at this index yet, this is the 1st node
            self.m[index] = ListNode(key, value)    # NEW
        else:                       # Already pair(key, val) at this index, Use Chaining to see if pair exists
            cur = self.m[index]
            while cur.__next__ is not None:
                if cur.pair[0] == key:          # this key exists
                    cur.pair = (key, value)     # UPDATE val
                    return
                cur = cur.__next__

            # key does not exists in chain. Add
            cur.next = ListNode(key, value)     # NEW: Collision

    def get(self, key):
        """
        Key will be at Index OR in case of collision of index, key will be part of chaining list.
        :param key: int
        :return: value int
        """
        index = key % self.capacity
        cur = self.m[index]
        while cur:
            if cur.pair[0] == key:  # Found key
                return cur.pair[1]
            else:
                cur = cur.__next__

        # key not found
        return -1

    def remove(self, key):
        return -1

    def printMap(self):
        print((self.m))


myHashMap = HashMap()
myHashMap.put(1, 1);          
myHashMap.put(2, 2);         
print(myHashMap.get(1));            # returns 1
print(myHashMap.get(3));            # returns -1 (not found)
myHashMap.put(2, 1);          # update the existing value
print(myHashMap.get(2));            # returns 1
myHashMap.remove(2);          # remove the mapping for 2
print(myHashMap.get(2));            # returns -1 (not found)
myHashMap.printMap()
