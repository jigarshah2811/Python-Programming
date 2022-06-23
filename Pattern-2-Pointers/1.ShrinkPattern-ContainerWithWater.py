"""
https://leetcode.com/problems/container-with-most-water/
Look at: https://leetcode.com/problems/container-with-most-water/solution/
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2-pointers shrink pattern
        # L ----> 
        # R <-------
        area, maxArea = 0, 0
        N = len(height)
        l, r = 0, N-1
        
        while l < r:
            # Calculate Area
            area = min(height[l], height[r]) * (r-l)
            # Keep track of maxArea
            maxArea = max(maxArea, area)
        
            # Take decision to move L---> OR <---- R so that area can be increased by getting to more height!
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return maxArea
                