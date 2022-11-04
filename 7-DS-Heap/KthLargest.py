""" DS: Heap 
    Pattern: MinHeap (To keep kth Largest in the fixed stream) 
             MaxHeap (To keep kth smallest in the fixed stream)

"""
import heapq
from typing import List

class SolutionWithMinHeap:
    def KthLargest(self, nums: List[int], k: int) -> int:
        # MinHeap: This will sort all nums
        heapq.heapify(nums)

        # Remove first len(nums)-K nums so that only K largest stays in heap
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]      # 1st largest on heap is Kth

s = SolutionWithMinHeap()
nums = [3,2,1,5,6,4]
k = 2
print(s.KthLargest(nums, k))      # output: 5

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(s.KthLargest(nums, k))      # output: 4


"""
   https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/
"""
class SolutionWithMaxHeap:    
    def KLargest(self, nums: List[int], K: int) -> List[int]:
        # MaxHeap of Size K 
        # to keep the max K numbers in heap!
        maxHeap = [0] * K
        for num in nums:
            # Trick: This adds an item and removes MIN item! Effectively making space for MAX items
            heapq.heappushpop(maxHeap, num)

        # Only K Largest numbers will stay in MaxHeap
        return [num for num in maxHeap]

s = SolutionWithMaxHeap()

arr = [1, 5, 4, 4, 2]; K = 2
print(s.KLargest(arr, K))       # Output: [4, 5]
arr = [1, 5, 1, 5, 1]; K = 3
print(s.KLargest(arr, K))       # Output: [5, 1]
