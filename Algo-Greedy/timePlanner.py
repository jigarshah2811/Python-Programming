class Solution(object):


    def planner(self, slotsA, slotsB, targetDuration):
        res = []

        a, b = 0, 0
        start, end = 0, 1

        while a < len(slotsA) and b < len(slotsB):
            A = slotsA[a]
            B = slotsB[b]
            if self.overlaps(A, B):
                print(("Overlapping found: SlotA: {0}, SlotB: {1}".format(A, B)))
                res = self.findDuration(A, B, targetDuration)
                if len(res) != 0:
                    return res

            # Move to find next overlap
            if B[start] <= A[start]:
                b += 1
            else:
                a += 1

        return res

    def overlaps(self, A, B):
        start, end = 0, 1

        print(("Checking overlap: {0} and {1}".format(A, B)))
        # If any point B[start] or B[end] is in middle of A[start] --> A[end] then it's overlapping
        if A[start] <= B[start] <= A[end] or A[start] <= B[end] <= A[end]:
            return True
        return False

    def findDuration(self, A, B, targetDuration):
        start, end = 0, 1

        print(("Checking duration {2} in overlap: {0} and {1}".format(A, B, targetDuration)))
        if B[end] >= A[start]:
            curDur = B[end] - A[start]
            if curDur >= targetDuration:
                # Bingo !
                return [A[start], A[start]+targetDuration]
        elif A[end] >= B[start]:
            curDur = A[end] - B[start]
            if curDur >= targetDuration:
                # Bingo
                return [B[start], B[start]+targetDuration]

        return []

s = Solution()

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
print(s.planner(slotsA, slotsB, 8))

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
print(s.planner(slotsA, slotsB, 12))
