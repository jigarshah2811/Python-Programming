class Solution(object):
    """
    Even on Left side, Odd on right side
    """
    def ArrangeEvenOdd(self, A):
        odd = 0
        for i in range(len(A)):
            if A[i] % 2 == 0:
                # Even Number, Swap with odd number to go Left !
                A[i], A[odd] = A[odd], A[i]

                # Next swap with this odd number
                odd += 1
        return A


    """
     https://leetcode.com/problems/move-zeroes/
     """
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i, zeroIndex = 0, -1

        for i in range(len(nums)):
            if zeroIndex == -1 and nums[i] == 0:
                zeroIndex = i
            elif zeroIndex != -1 and nums[i] != 0:
                nums[i], nums[zeroIndex] = nums[zeroIndex], nums[i]
                zeroIndex += 1
            else:
                continue

    def removeLeadingZeros(self, A = list()):
        for i in range(len(A)):
            if A[i] != 0:
                # Just return entire array from this first non-zero index
                return A[i:len(A)]

s = Solution()
A = [2, 7, 3, 1, 9, 4]
print(s.ArrangeEvenOdd(A))
A = [3, 7, 3, 1, 9, 4]
print(s.ArrangeEvenOdd(A))
A = [2, 4, 6, 8, 9]
print(s.ArrangeEvenOdd(A))


nums = [0,1,0,3,12]
print((s.moveZeroes(nums)))

A = [0, 0, 0, 1, 2, 3]
print(s.removeLeadingZeros(A))
A = [0, 0, 0, 1, 0, 2, 3]
print(s.removeLeadingZeros(A))
