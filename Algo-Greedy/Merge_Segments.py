"""
https://leetcode.com/discuss/interview-question/322054/LinkedIn-or-Merge-Segments

Data Structure: Sorted Segments (Intervals)
Add() ---> InsertionSort
Get() ---> Get the size of all intervals
Optimization ---> During Get(), it actually Merges overlapping intervals to keep final SortedSegments Array Small! So adds are faster!
"""


class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class DownloadTask():
    def __init__(self):
        self.sortedSegs = []
        self.size = 0

    def add(self, newSeg: Segment) -> None:
        if len(self.sortedSegs) == 0:   # First segement
            self.sortedSegs.append(newSeg)
            return

        # All sub-sequent segements
        insertPos, i = -1, 0
        while i < len(self.sortedSegs):
            if newSeg.start < self.sortedSegs[i].start:
                insertPos = i
                break
            i += 1

        # Insert at i-1 th place
        if insertPos == -1:         # Insert at End
            self.sortedSegs.append(newSeg)
        else:                       # Insert at insertPos
            self.sortedSegs.insert(insertPos, newSeg)

        # Debugging
        print("After Add:")
        for seg in self.sortedSegs:
            print((seg.start, seg.end),)

    def getFileSize(self) -> int:
        merged = [self.sortedSegs[0]]
        self.size = merged[0].end - merged[0].start

        for i, seg in enumerate(self.sortedSegs):
            if i == 0:
                continue

            if seg.start <= merged[-1].end: # Overlapping with prev
                self.size += seg.end - merged[-1].end
                merged[-1].end = max(merged[-1].end, seg.end)
            else:
                merged.append(seg)
                self.size += seg.end - seg.start

        self.sortedSegs = merged
        return self.size

task = DownloadTask()
task.add(Segment(1, 5))
task.add(Segment(4, 6))
print(task.getFileSize())  # returns 5
task.add(Segment(10, 20))
task.add(Segment(25, 39))
print(task.getFileSize())  # returns 29
task.add(Segment(19, 25))
print(task.getFileSize())  # returns 34
