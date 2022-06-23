from typing import List

class Solution:
    def BinarySearch(self, nums: List[int], target: int) -> int:
            # Binary search works only for sorted array, so make sure array is sorted
        # Setup indexes, low and high and move them around low++ or high-- based on mid value
        low, high = 0, len(nums)-1

        while low <= high:
            mid = low // 2   # Works for even and odd size arr pretty well, left side will have 1 more element
            if nums[mid] == target:   # FOUND!
                return mid
            elif nums[mid] > target:  # We are too much on right side, move to left
                high = mid-1   # <---- High
            else:               # We are too much on left side, move to right
                low = mid+1    # Low ---->
        
        return -1   # if target element not found, return -1 == NOT_FOUND
    

s = Solution()

arr  = [1, 2, 3, 4, 5, 6, 7]
print(s.BinarySearch(arr, target=6))

arr = [-1,0,3,5,9,12]
print(s.BinarySearch(arr, target=9))
