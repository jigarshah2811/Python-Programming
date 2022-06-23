"""
STRATEGY: Modify as you go...
"""
class Solution(object):
    def plusOne(self, digit):
        """
        :type digit: List[int]
        :rtype: List[int]
        """
        n = len(digit)-1
        # Traverse list in reverse
        for i in range(n, -1, -1):
            if digit[i] < 9:
                digit[i] += 1
                return digit
            digit[i] = 0

        digit.insert(0, 1)
        return digit

s = Solution()
arr = [1,2,3,4]
print(s.plusOne(arr))
arr = [1,2,3,9]
print(s.plusOne(arr))
arr = [9,9,9,9]
print(s.plusOne(arr))
