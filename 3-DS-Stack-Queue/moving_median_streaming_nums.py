import collections
import math
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.purge = True
        self.q = collections.deque()
        self.median = 0.0
        self.medianAtStart = False
        self.purge = True

    def addNum(self, num: int) -> None:
        if len(self.q) < 2:
            self.q.append(num)
            print(("Initial addNum q:{}".format(self.q)))
            if len(self.q) % 2: # Odd
                self.medianAtStart = True
            else:
                self.medianAtStart = False
            return

        self.q.append(num)

        if self.purge:     # odd
            self.q.popleft()
            self.medianAtStart = True

        self.purge = not self.purge
        print(("addNum q:{}".format(self.q)))

    def findMedian(self) -> float:
        if not self.medianAtStart:
            self.median = (self.q[0] + self.q[1]) / 2
            print(("Even findMedian: q: {} {} median: {}".format(self.q, len(self.q), self.median)))
        else:
            self.median = self.q[0]
            print(("Odd findMedian: q: {} {} median: {}".format(self.q, len(self.q), self.median)))

        return float(format(self.median, '.2f'))

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
s = MedianFinder()
s.addNum(1)
s.addNum(2)
print((s.findMedian())) # -> 1.5
s.addNum(3)
print((s.findMedian())) # -> 2

s1 = MedianFinder()
arr = [-1, -2, -3, -4, -5]
for num in arr:
    s1.addNum(num)
print((s1.findMedian()))
