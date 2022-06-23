class Solution(object):
    def findMaxFlowerBed(self, arr):
        counter = 0
        for i in range(len(arr)-1):
            if self.isSafe(i, arr):
                arr[i] = 1
                counter += 1
        return counter

    def isSafe(self, index, arr):
        startIndex = 0
        endIndex = len(arr) - 1
        if (index == startIndex or arr[index] != 1) and arr[index-1] != 1 and (index == endIndex or arr[index+1] != 1):
            #print index,
            return True
        else:
            return False

arr = [1,0,1,0,0,0,0,0,1,1,0,0,0,1]
assert(Solution().findMaxFlowerBed(arr) == 3)

arr = [0,0,0,1,1,1,0,0,1,1,0,0,0,0,1,1,1,0,0,0]
assert(Solution().findMaxFlowerBed(arr) == 3)
