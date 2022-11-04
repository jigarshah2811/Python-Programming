from typing import List


class Solution1:
    def combinationSum1(self, nums, target):
        def isSafe(num, target):
            if target-num >= 0:
                return True
            return False

        def dfs(begin, res, target):
            if target == 0:
                finalResult.append(res[:])
                return
            for i, num in enumerate(nums, start=begin):
                if isSafe(num, target)
                    res.append(num)
                    dfs(begin=i, res=res, target=target-num)    # Depth = Same Level! Since dups are allowed.
                    res.pop()

        finalResult = []
        nums.sort()             # Sorting to speedup. Limit range of nums to include in target, outside the range cannot be in our solution
        dfs(target, 0, [])
        return finalResult


class Solution2:
    def combinationSum2(self, nums, target):
        def isSafe(num, target):
            if target-num >= 0:
                return True
            return False

        def dfs(target, index, res):
            if target == 0:
                finalResult.append(res[:])
                return
            for i in range(index, len(nums)):
                if nums[i] > target:  # Optimization: Arr is sorted, so if nums[i] makes target >, skip all next nums
                    break
                if isSafe(nums[i], target):
                    res.append(nums[i])
                    dfs(target-nums[i], i+1, res)     # Dups allowed, so depth with the same index to try same num again
                    res.pop()

        finalResult = []
        nums.sort()             # Sorting to speedup. Limit range of nums to include in target, outside the range cannot be in our solution
        dfs(target, 0, [])

        # Remove dup solutions
        newRes = []
        for res in finalResult:
            if res not in newRes:
                newRes.append(res)

        print(("FinalResult: {}".format(finalResult)))
        print(("NewResult: {}".format(newRes)))
        return newRes


class Solution3:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        def isSafe(num, target):
            if target - num >= 0:
                return True
            return False

        def dfs(target, index, res):
            if target == 0 and len(res) == k:
                finalResult.append(res[:])
                return
            for i in range(index, len(nums)):
                if nums[i] > target:
                    break
                if isSafe(nums[i], target):
                    res.append(nums[i])
                    dfs(target - nums[i], i + 1, res)  # Dups allowed, so depth with the same index to try same num again
                    res.pop()

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        finalResult = []
        dfs(target, 0, [])

        # Remove dup solutions
        newRes = []
        for res in finalResult:
            if res not in newRes:
                newRes.append(res)
        return newRes


class Solution4:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def backtrack(target):
            for num in nums:
                if num > target: break
                if num == target:
                    res.append('A')
                if num < target:
                    backtrack(target - num)

        res = []
        nums.sort()
        backtrack(target)
        print(res)
        return len(res)

"""
DP
"""
class Solution5(object):
    def combinationSum5(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]

# 17 / 17 test cases passed.
# Status: Accepted
# Runtime: 116 ms

# s = Solution1()
# print(s.combinationSum1(nums=[2,3,5], target=8))
# print(s.combinationSum1(nums=[2, 3, 6, 7], target=7))
#
# s = Solution2()
# print(s.combinationSum2(nums=[2,3,5], target=8))
# print(s.combinationSum2(nums=[2, 3, 6, 7], target=7))
#
# s = Solution3()
# print(s.combinationSum3(k=3, target=7))
# print(s.combinationSum3(k=3, target=9))
s = Solution4()
print((s.combinationSum4(nums=[1, 2, 3], target=4)))
#print(s.combinationSum4(nums=[4, 2, 1], target=32))