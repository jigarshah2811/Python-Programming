class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def percUp(self,i):
        while i // 2 > 0:
          print(f"Heap: {self.heapList} Checking value: {self.heapList[i]} at index: {i} and ParentIndex: {i//2}")
          if self.heapList[i] < self.heapList[i // 2]:
             tmp = self.heapList[i // 2]
             self.heapList[i // 2] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heapList[i*2] < self.heapList[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

bh = BinHeap()
arr = [5, 2, 1, 4, 3]
for item in arr:
    bh.insert(item)
print(f"Heap: {bh.heapList}")
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())


class MinHeap:
    """ Root is always greater then all children 
        Balanced Binary Tree (L & R are always less then root)
    """
    def __init__(self) -> None:
        self.h = [0]
        self.currentSize = 0
    
    def insert(self, item):
        self.h.append(item)
        self.currentSize += 1
        self.bubbleUp(self.currentSize)

    def bubbleUp(self, index):
        # Bubble up item until it reaches to it's final position according to HEAP PROPERTY 
        while  index // 2 > 0:
            print(f"Heap: {self.h} Checking value: {self.h[index]} at index: {index} and ParentIndex: {index//2}")
            if self.h[index] < self.h[index // 2]:  # Parent is large! Breaking heap property
                # Swap newly added item with it's parent if it's smaller
                self.h[index], self.h[index // 2] = self.h[index // 2], self.h[index]
            
            index = index // 2      # Keep comparing with parent
        #print(f"Added value: {item}, heap: {self.h}")

minHeap = MinHeap()
arr = [5, 2, 1, 4, 3]
for item in arr:
    minHeap.insert(item)
print(f"minHeap: {minHeap.h}")