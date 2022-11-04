""" Q: Partition Array so that Sum of all partitions are SAME

Given an array of integers greater than zero, find if there is a way to
split the array in two (without reordering any elements) such that the
numbers before the split add up to the numbers after the split. If so,
print the two resulting arrays.

=== Test cases ===

In [1]: can_partition([5, 2, 3]) 
Output [1]: ([5], [2, 3]) 
Return [1]: True 
 
In [2]: can_partition([2, 3, 2, 1, 1, 1, 2, 1, 1]) 
Output [2]([2, 3, 2], [1, 1, 1, 2, 1, 1]) 
Return [2]: True 

In [3]: can_partition([1, 1, 3]) 
Return [3]: False 

In [4]: can_partition([1, 1, 3, 1]) 
Return [4]: False
""" 

class Solution:
    def can_partition(self, nums):
        Lsum, Rsum = 0, sum(nums)
        for i, num in enumerate(nums):
            Lsum += num
            Rsum -= num

            if Lsum == Rsum:
                print(f"Found split at:{i}, LeftSum: {Lsum}, RightSum: {Rsum}")
                L = nums[:i+1]    # <--- ..i        (includes 0.....i)
                R = nums[i+1:]    # ---->    i...   (includes i+1....)
                return(L, R)
        
        return None

s = Solution()

nums = [5, 2, 3]
print(s.can_partition(nums))    # output Output [1]: ([5], [2, 3]) 

nums = [2, 3, 2, 1, 1, 1, 2, 1, 1]
print(s.can_partition(nums))    # output ([2, 3, 2], [1, 1, 1, 2, 1, 1]) 

nums = [1, 1, 3]
print(s.can_partition(nums))    # output: None, FALSE
nums = [1, 1, 3, 1]
print(s.can_partition(nums))    # Output: None, False