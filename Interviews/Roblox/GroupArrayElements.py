from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        def swap(i, j):
            while i < j:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                i += 2
                
        for i in range(n-1):
            print(f"{i}")
            swap(n-1-i, n+i)
        return nums

s = Solution()
nums = [1, 2, 3, 4, 5, 6]; n = 3
print(s.shuffle(nums, n))