"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646/
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
"""
class Solution:
    def rotate(self, arr, k):
        k = k % len(arr)
        if k > len(arr):
            return arr
        self.arrReverse(arr, 0, len(arr) - 1)
        self.arrReverse(arr, 0, k - 1)
        self.arrReverse(arr, k, len(arr) - 1)

    def arrReverse(self, arr, low, high):
        while low < high:
            arr[low], arr[high] = arr[high], arr[low]
            low += 1
            high -= 1



s = Solution()
arr = [1,2,3,4,5,6,7]
s.rotate(arr, 3)
print(arr)


arr = [-1]
s.rotate(arr, 3)
print(arr)
