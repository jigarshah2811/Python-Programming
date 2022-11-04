"""
https://www.geeksforgeeks.org/find-maximum-product-of-a-triplet-in-array/
"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        nums = sorted(nums, reverse=True)
        total = len(nums)
        print nums

        # All Positives
        for i in xrange(0, total):
            if nums[i] > 0:
                result.append(nums[i])
            else:
                nagativeStartPos = i
                break

        print "Positives Added..."
        print result
        print "Loop for nagativeNums From %s to %s"%(total, nagativeStartPos)
        for i in xrange(total-1, nagativeStartPos-1, -1):
            print "To be added ", nums[i]
            result.append(nums[i])
            if len(result) >= 3:
                break

        print result
        return reduce(lambda x, y: x * y, result)


s = Solution()
nums = [-1, -2, -3]
print s.maximumProduct(nums)
