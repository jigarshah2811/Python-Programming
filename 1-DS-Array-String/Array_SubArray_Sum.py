"""
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
"""
class Solution:
    def shortestSubarray(self, nums, k):
        contiguousSum, count, minCount = 0, 0, float('inf')

        begin = 0

        for end, num in enumerate(nums):
            contiguousSum += num

            if k == num:    # A num itself is k, return 1
                return 1
            elif contiguousSum >= k:
                count += 1

                while contiguousSum >= k:
                    contiguousSum -= nums[begin]
                    begin += 1

                # Track minCount
                minCount = min(minCount, end-begin)
                count, contiguousSum, begin = 0, 0, end

            elif abs(k - contiguousSum) <= abs(k - num): #keep going
                count += 1
            else: # restart
                count = 1
                contiguousSum = num

            print(("contiguousSum:{0}, count:{1}, minCount: {2}".format(contiguousSum, count, minCount)))
        return -1 if minCount == float('inf') else minCount


s = Solution()
# print(s.shortestSubarray([1], 1))
# print(s.shortestSubarray([1, 2], 4))
# print(s.shortestSubarray([2, -1, 2], 3))
# print(s.shortestSubarray([48,99,37,4,-31],140))
print((s.shortestSubarray([48,99,37,4,-31], 140)))