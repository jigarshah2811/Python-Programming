"""
https://leetcode.com/problems/merge-intervals/
252 Meeting Rooms
253 Meeting Rooms II
435 Non-overlapping Intervals <- very similar, i did it with just 3 lines different
"""
class Solution(object):
    def mergeIntervals(self, intervals):

        intervals = sorted(intervals, key=lambda interval: interval.start)
        merged = []

        for interval in intervals:
            # Not overlapping with existing interval, then create new intervval
            if not merged or merged[-1].end > interval.start:
                merged.append(interval)
            else:
                # Overlapping: So just update last merged interval's end to extend range
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged


s = Solution()
intervals = [[2,6],[8,10],[15,18],[1,3]]
intervals = [(2,6),(8,10),(15,18),(1,3)]
print(s.mergeIntervals(intervals))

intervals = [[1,4],[4,5]]
#print s.mergeIntervals(intervals)