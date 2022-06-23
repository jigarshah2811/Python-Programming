from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Shrinking 2 pointers pattern! Multiple Pass L ---->   <-----R  then result ------> Pattern

        https://leetcode.com/problems/trapping-rain-water/
        """
        N = len(nums)
        L, R, res = [1]*N, [1]*N, [1]*N

        # L -----> Traverse front
        # Left Product at i is: Prefix product of i-1 * previous num
        for i in range(1, N):
            L[i] = L[i-1] * nums[i-1]

        # <---------R Traverse back 
        # Right Product at i is: Prefix product until i+1 * previous num
        for i in range(N-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]


        # L[i] has product of all numbers till i
        # R[i] has product of all numbers till i
        # Result is simply L[i] (prefix product of all L) * R[i] (prefix product of all R)
        for i in range(N):
            res[i] = L[i] * R[i]

        return res

    def productExceptSelfOptimized(self, nums: List[int]) -> List[int]:
        """ 
        Optimized version O(1) space
        L ----> 
        Result while R <-------
        """
        N = len(nums)
        res = [1]*N

        # L -----> Traverse front
        # Left Product at i is: Prefix product of i-1 * previous num
        for i in range(1, N):
            res[i] = res[i-1] * nums[i-1]
        print(res)
            
        # <---------R Traverse back 
        # Right Product at i is: Prefix product until i+1 * previous num
        rMax = 1
        for i in range(N-1, -1, -1):
            # Result at i is: L prefix product till now (res[i]) * Right prefix product till now (rMax)
            res[i] = res[i] * rMax
            
            # Update max R prefix product to carry forward
            rMax = rMax * nums[i]
            print(res[i], rMax)

        return res

            