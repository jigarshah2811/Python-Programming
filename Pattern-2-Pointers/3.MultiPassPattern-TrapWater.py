"""
Shrinking 2 pointers pattern! Multiple Pass L ---->   <-----R  then result ------> Pattern

https://leetcode.com/problems/trapping-rain-water/

"""
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        leftMax = [0]*N
        rightMax = [0]*N
        
        leftMax[0] = height[0]
        for i in range(1, N):
            leftMax[i] = max(leftMax[i-1], height[i])
        
        rightMax[N-1] = height[N-1]
        for i in range(N-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])
            
        print(f"leftMax: {leftMax}")
        print(f"rightMax: {rightMax}")
        
        # Add water from either L bar or R bar depending on which has less Max
        res = 0
        for i in range(N):
            # At i -> look at LeftMax height and RightMax height
            # Fill water: that can be trappped at this point is (Lmax-Rmax) and some height may already be tehre, so
            water = min(leftMax[i], rightMax[i]) - height[i]
            res += water
        
        return res
            