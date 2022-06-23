from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if len(intervals) == 0:  # This is 1st interval
            intervals.append(newInterval)
            return intervals

        start, end = 0, 1

        mergeBeginPos, i = -1, 0
        while i < len(intervals):
            if newInterval[start] < intervals[i][start]:  # Overlap finished for start
                mergeBeginPos = i
                break
            i += 1

        if mergeBeginPos == -1:  # Reached End, No merge neccesary
            intervals.append(newInterval)
            return intervals

        mergeBeginPos -= 1          # ONE STEP LESS?

        mergeEndPos, i = len(intervals)-1, mergeBeginPos
        while i < len(intervals):
            if newInterval[end] < intervals[i][end]:  # Overlap finished for start
                mergeEndPos = i
                break
            i += 1

        mergeEndPos -= 1          # ONE STEP LESS?

        print("MergeBegin: {}, MergeEnd: {}".format(mergeBeginPos, mergeEndPos))
        # The overlapping intervals are from (mergeBeginPos - mergeEndPos)
        # Merge them
        intervals[mergeEndPos][start] = min(intervals[mergeBeginPos][start], newInterval[start])
        intervals[mergeEndPos][end] = max(intervals[mergeEndPos][end], newInterval[end])

        # Remove all intermittent intervals and get this final one
        #del intervals[mergeBeginPos: mergeEndPos]

        return intervals

s = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(s.insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
ewInterval = [4,8]
print(s.insert(intervals, newInterval))