"""
Kth Smallest/Largest element from un-sorted array

https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

Solution:
QuickSort optimization: We find PivotIndex at the end of partition method that's final position for pivot.
                        simply return if that's K
                        If not, sort ONLY Left or Right array based on where K lies in-respect of pi returned
"""

class QuickSelect:
    def findKthLargest(self, nums: list, k: int) -> int:
        # Quick Sort: For Nums, Low to High....
        def quickselect(nums, start, end, k):
            # Base case
            # print(start,end)
            if start < end:  # PreOrder, CLR Traversal
                pi = partition(nums, start, end)

                """ TRICK: OPTIMIZATION - QuickSelect 
                If the pi index is what we are looking for, break! """
                if pi == kthHighIndex:
                    return nums[pi]

                # Recur for L sub-array and R sub-array
                quickselect(nums, start, pi - 1, k)
                quickselect(nums, pi + 1, end, k)

            return nums[kthHighIndex]   # In worst case: The kth highest was sorted at last after entire arr!

        def partition(nums, start, end):
            pivot, pi = nums[end], start

            for i in range(start, end):
                if nums[i] < pivot:
                    nums[i], nums[pi] = nums[pi], nums[i]
                    pi += 1

            # NOw pi will be the final position for pivot
            nums[pi], nums[end] = nums[end], nums[pi]
            return pi

        kthHighIndex = len(nums) - k
        
        # Quick Sort: For Nums, Low to High.....
        return quickselect(nums, 0, len(nums) - 1, k)


q = QuickSelect()
arr = [6,7,1,2,4,5,3]
k = 4
print(q.findKthLargest(arr))