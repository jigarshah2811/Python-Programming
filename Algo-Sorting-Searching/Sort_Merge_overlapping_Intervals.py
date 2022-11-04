"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""

# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        sortedIntervals = sorted(intervals, key=lambda x: x.start)
        merged = []
        prevInterval = sortedIntervals[0]

        for interval in sortedIntervals:
            """
            Now the intervals will be in sorted order
            Means, nextInterval.start will always be > previousInterval.start
            """
            # 1st interval
            if not merged:
                merged.append(interval)
                continue

            # Check this interval can NOT be merged
            if interval.start > merged[-1].end:
                # NOT overlapping
                merged.append(interval)
            else:
                # Overlapping interval
                merged[-1].end = max(interval.end, prevInterval.end)


        return merged

    def printIntervals(self, intervals):
        for interval in intervals:
            print("[{0},{1}]".format(interval.start, interval.end))

print("Merging intervals")
s = Solution()
intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15,18)]
s.printIntervals(s.merge(intervals))

print("Merging intervals")
intervals = [Interval(1,9), Interval(2,5), Interval(19,20), Interval(10,11), Interval(12,20), Interval(0,3), Interval(0,1),Interval(0,2)]
s.printIntervals(s.merge(intervals))

