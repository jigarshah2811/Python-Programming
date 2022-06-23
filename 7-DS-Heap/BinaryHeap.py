class BinHeap:
    def __init__(self):
        self.heap = [0]
        self.currentSize = 0

    def bubbleUp(self, i):
        parent = (i // 2)
        while parent > 0:
            if self.heap[i] < self.heap[parent]:    # If this val is less then parent
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]   # Swap with parent
            i = parent

    def bubbleDown(self, i):
        child = i * 2
        while child <= self.currentSize:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:        # If this val is greater then child
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]   # Swap with child
            i = mc

    def percUp(self,i):
        while i // 2 > 0:
          if self.heap[i] < self.heap[i // 2]:
             tmp = self.heap[i // 2]
             self.heap[i // 2] = self.heap[i]
             self.heap[i] = tmp
          i = i // 2

    def insert(self,k):
      self.heap.append(k)
      self.currentSize = self.currentSize + 1
      self.bubbleUp(self.currentSize)

    def percDown(self,i):
      while (i * 2) <= self.currentSize:
          mc = self.minChild(i)
          if self.heap[i] > self.heap[mc]:
              tmp = self.heap[i]
              self.heap[i] = self.heap[mc]
              self.heap[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * 2 + 1 > self.currentSize:
          return i * 2
      else:
          if self.heap[i*2] < self.heap[i*2+1]:
              return i * 2
          else:
              return i * 2 + 1

    def delMin(self):
      try:
        retval = self.heap[1]
      except:
          print("Key Error: Is heap empty?")
          return -1

      self.heap[1] = self.heap[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heap.pop()
      self.bubbleDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // 2
      self.currentSize = len(alist)
      self.heap = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

bh = BinHeap()
bh.buildHeap([9,5,6,2,3])

print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
bh.insert(1)
bh.insert(2)
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
print(bh.delMin())
