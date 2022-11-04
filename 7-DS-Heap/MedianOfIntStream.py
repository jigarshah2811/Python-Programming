""" DS: Heap  Pattern: MinHeap + MaxHeap & Rebalance to keep top K MinVal and Top MaxVal for use

https://leetcode.com/problems/find-median-from-data-stream/
"""
import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # Initialize: Add first number in maxHeap
        if len(self.min_heap) + len(self.max_heap) <= 1:
            heapq.heappush(self.max_heap, num)
            return
        
        # Add "lower" num to maxHeap and "higher" num to minHeap
        median = self.findMedian()
        if num >= median:
            heapq.heappush(self.min_heap, num)
        else:
            heapq.heappush(self.max_heap, num)
        
    def rebalance(self):
        if len(self.max_heap) > len(self.min_heap) + 1: # maxHeap is growing!
            # Remove from maxHeap --> Add in minHeap
            num = heapq.heappop(self.max_heap)  
            heapq.heappush(self.min_heap, num)
        elif len(self.min_heap) > len(self.max_heap) + 1: # minHeap is growing!
            # Remove from minHeap --> Add in maxHeap
            num = heapq.heappop(self.min_heap)  
            heapq.heappush(self.max_heap, num)
        else:
            print(f"Already balanced: minHeap: {(self.min_heap)} and maxHeap: {(self.max_heap)}")
        
        print(f"After Rebalance: minHeap: {(self.min_heap)} and maxHeap: {(self.max_heap)}")

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            maxVal = heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap, maxVal)
            return maxVal
        elif len(self.min_heap) > len(self.max_heap):
            minVal = heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, minVal)
            return minVal
        else:       # Even case: So median is minVal + maxVal // 2
            maxVal = heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap, maxVal)
            minVal = heapq.heappop(self.min_heap)            
            heapq.heappush(self.min_heap, minVal)
            return ((minVal + maxVal) / 2)
        
# Your MedianFinder object will be instantiated and called as such:
medianFinder =  MedianFinder()
nums = [1, 2, 3, 5, 7]
for num in nums:
    print(f"adding {num}")
    medianFinder.addNum(num)
    medianFinder.rebalance()
    print(f"Median: {medianFinder.findMedian()}")
