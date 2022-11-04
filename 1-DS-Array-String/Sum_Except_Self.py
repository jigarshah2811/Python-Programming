class Solution:
    def productExceptSelf(self, nums):
        # Create L arr, where L[i] is sum of nums[0...i-1]
        # Create R arr, where R[i] is sum of nums[len(n)...i]
        if len(nums) == 0:
            return []
        L, R, res = [1]*len(nums), [1]*len(nums), [1]*len(nums)

        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]



        print(("L = {0}".format(L)))
        print(("R = {0}".format(R)))

        for i in range(len(nums)):
            res[i] = L[i] * R[i]

        return res

s = Solution()
print(s.productExceptSelf([1,2,3,4,5]))
print(s.productExceptSelf([4, 5, 1, 8, 2, 10, 6]))
print(s.productExceptSelf([]))
print(s.productExceptSelf([0]))
