from collections import deque, defaultdict, OrderedDict

class LRUCacheOrderedDict:
    ERROR_KEY_NOT_EXISTS = -1
    def __init__(self, capacity=3) -> None:
        self.lru = OrderedDict()
        self.capacity = capacity
    
    def set(self, key, val):
        if key in self.lru:     # If already exists, remove the key and set the new {key: val} pair
            del self.lru[key]
        self.lru[key] = val     # This will move the END of dict in-order
        
        # Check if capacity is full
        if len(self.lru) > self.capacity:   # Need to purge LRU entry that's stored in order (FIFO)
            self.lru.popitem(last=False)
    
    def get(self, key):
        # Check if key does not exists
        if key not in self.lru: return self.ERROR_KEY_NOT_EXISTS

        # If key exists, move this key to END in ordered dict as it's most recently used
        val = self.lru[key]
        
        # Remove from middle, move to end
        del self.lru[key]
        self.lru[key] = val
        
        return val

    def prettyprint(self):
        for key, val in self.lru.items():
            print(f"{key} --> {val}")


class Node:
    def __init__(self, key, val, prev, next) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:
    def __init__(self, capacity) -> None:
        self.lru = defaultdict(None)
        self.capacity = capacity
        
        # Create a LL with dummy Head and Tail - connect them
        # All Node operations Add/Remove will be performed as middle nodes!
        self.head = Node(0, 0, None, None)
        self.tail = Node(0, 0, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key not in self.lru: return -1
        node = self.lru[key]
        self.removeNode(node)
        self.addNode(node)
        return node.val
    
    def set(self, key, val):
        if key in self.lru: self.removeNode(self.lru[key])

        newNode = Node(key, val, None, None)
        self.addNode(newNode)
        self.lru[key] = newNode

        # Purge if cache is full
        self.purge()
    
    def purge(self):
        while len(self.lru) > self.capacity:
            staleNode = self.head.next
            del self.lru[staleNode.key]
            self.removeNode(staleNode)

    def addNode(self, node):    # Add node just before tail
        beforetail = self.tail.prev  # save tail's prev before changing
        beforetail.next = node
        self.tail.prev = node
        node.prev = beforetail
        node.next = self.tail
    
    def removeNode(self, node):
        beforeNode = node.prev
        afterNode = node.next
        afterNode.prev = beforeNode
        beforeNode.next = afterNode

    def prettyprint(self):
        for key, node in self.lru.items():
            print(f"{key} --> {node.val}")

lruCache = LRUCache(capacity=3)
lruCache.set(1, 'A'), lruCache.set(2, 'B'), lruCache.set(3, 'C')
print("After sets")
lruCache.prettyprint()
lruCache.get(3), lruCache.get(1)
print("After gets")
lruCache.prettyprint()
print("After running over capacity and set")
lruCache.set(4, 'D')        # Key 'B' should be removed since 'B' and 'C' were later used
lruCache.prettyprint()
 # doesn't exists
print(f"get(key) that doesn't exists: {lruCache.get(5)}")
lruCache.prettyprint()
