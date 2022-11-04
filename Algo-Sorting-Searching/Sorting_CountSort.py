"""
Count Sort

https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/798/

https://www.programcreek.com/2014/06/leetcode-sort-colors-java/

https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
"""

class CountSort(object):
    def __init__(self):
        self.NUM_COLORS = 3

    def countSorting(self, nums):
        # Step 1: Freq counter for each number
        freq = [0]*self.NUM_COLORS
        for num in nums:
            freq[num] += 1

        index = 0
        k = 0
        while (index < self.NUM_COLORS):
            if freq[index]:
                nums[k] = index
                k += 1
                freq[index] -= 1
            else:
                index += 1
        return nums

cs = CountSort()
nums = [2,0,2,1,1,0]
print(cs.countSorting(nums))