"""
###### Maximum product of a triplet #######

Given an integer array, find a maximum product of a triplet in array.

Examples:

Input:  [10, 3, 5, 6, 20]
Output: 1200
Multiplication of 10, 6 and 20

Input:  [-10, -3, -5, -6, -20]
Output: -90

Input:  [1, -4, 3, -6, 7, 0]
Output: 168

https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/
"""

"""
STRATEGY: keep track as you go.. (Keep track of 1st max, 2nd max, 3rd max as you go...)
"""
class Solution(object):
    def findTripetWithMaxProduct(self, nums):
        if len(nums) < 3:
            return -1

        # Find max, second max, third max from Array
        maxA = maxB = maxC = float('-inf')

        # Find min, second min from array
        minA = minB = float('inf')

        for num in nums:

            # Update highest max
            if num > maxA:
                maxC = maxB
                maxB = maxA
                maxA = num
            # Update second highest max
            elif num > maxB:
                maxC = maxB
                maxB = num
            # Update third highest max
            elif num > maxC:
                maxC = num

            # Update lowest min
            if num < minA:
                minB = minA
                minA = num
            # Update second lowest min
            elif num < minB:
                minB = num
            else:
                continue

        # If all nums are Positives/Negatives, 3 highest nums makes max product
        maxWithPositives = maxA * maxB * maxC
        # If at-least 2 negative nums (but not all), 2 negatives and 1 max positive makes max product
        maxWithNegatives = maxA * minA * minB

        return max(maxWithPositives, maxWithNegatives)


    def findTripetWithMaxProduct_Sort(self, nums):
        if len(nums) < 3:
            return -1

        # Find max, second max, third max from Array
        maxA = maxB = maxC = float('-inf')

        # Find min, second min from array
        minA = minB = float('inf')

        n = len(nums)
        nums = sorted(nums)

        maxWithPositives = nums[n-1] * nums[n-2] * nums[n-3]
        maxWithNegatives = nums[0] * nums[1] * nums[n-1]

        return max(maxWithPositives, maxWithNegatives)



s = Solution()
nums = [1, -4, 3, -6, 7, 0]
print(s.findTripetWithMaxProduct(nums))
print(s.findTripetWithMaxProduct_Sort(nums))