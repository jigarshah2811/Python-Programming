class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Edge cases
        N = len(nums)
        if N <= 1:
            return 0    # The element at index 0 is peak!
        
        # Since we'r checking mid+1 and mid-1 in our solution, we have to cover 0th and N-1th position
        if nums[0] > nums[1]:
            return 0
        if nums[N-1] > nums[N-2]:
            return N-1
        
        # Now regular binary search for indexes between 1 to N-1
        low, high = 1, N-2
        while low <= high:
            mid = low + (high-low) // 2
            # Case 1: mid is greater then both neighbors     -  mid is peak!
            # Example [5, 6, 4]
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            # Case 3: ASCENDING
            # mid is less then "next" neighbor: peak is on -----> right
            # Example: [3, 5, 6]
            elif nums[mid] < nums[mid+1]:
                low = mid+1
                
            # Case 2: DESCENDING 
            # mid is less then "prev" neighbor: peak is on <---- left
            # Example: [6,4,1]
            # elif nums[mid] < nums[mid-1]:
            else:
                end = mid-1
                
        return low if nums[low] >= nums[high] else high