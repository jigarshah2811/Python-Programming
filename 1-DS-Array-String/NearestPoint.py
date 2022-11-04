"""
https://leetcode.ca/2021-05-01-1779-Find-Nearest-Point-That-Has-the-Same-X-or-Y-Coordinate/

Find Nearest Point That Has the Same X or Y Coordinate
"""
from typing import List

class Solution:
    def nearestDistance(self, points: List, targetPoint: tuple) -> int:
        dist, minDist = float('inf'), float('inf')

        (targetX, targetY) = targetPoint
        for (pointX, pointY) in points:
            # If this point overlaps with X or Y of target
            if pointX == targetX or pointY == targetY: 
                dist = self.calcManhattenDistance(pointX, pointY, targetX, targetY)
                minDist = min(minDist, dist)
        
        return minDist
    
    def calcManhattenDistance(self, pointX, pointY, targetX, targetY):
        return abs(pointX - targetX) + abs(pointY - targetY)

s = Solution()
x = 3; y = 4; points = [(1,2),(3,1),(2,4),(2,3),(4,4)]
print(s.nearestDistance(points, (x, y)))

x = 3; y = 4; points = [(3, 4)]
print(s.nearestDistance(points, (x, y)))

x = 3; y = 4; points = [(2, 3)]
print(s.nearestDistance(points, (x, y)))
