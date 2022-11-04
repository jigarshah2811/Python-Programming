import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ADD, REMOVE = 1, -1
        h = []
        heights = []
        res = []

        for [start, end, height] in buildings:
            heapq.heappush(h, [start, ADD, height])
            heapq.heappush(h, [end, REMOVE, height])
        heapq.heapify(h)

        while h:
            [point, add, height] = heapq.heappop(h)

            if add == ADD:  # New building started, Add it's height in current set of live heights, result height for point would be max of current set
                heights.append(height)
            else:           # Building ended, Remove it's height from current set of live heights, result height for point would be max of current set
                heights.remove(height)
            if len(heights):
                maxHeight = max(heights)
                if len(res) == 0:                   # 1st building
                    res += [[point, maxHeight]]
                elif res[-1][1] != maxHeight:
                    res += [[point, maxHeight]]
                else:                             # Same height as prev building, so skip
                    continue
            else:
                res += [[point, 0]]

        return res

s = Solution()
print(s.getSkyline(buildings=[ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ] ))

