class Solution(object):
    def removeLeadingZeros(self, A = list()):
        for i in xrange(len(A)):
            if A[i] != 0:
                # Just return entire array from this first non-zero index
                return A[i:len(A)]


s = Solution()
A = [0, 0, 0, 1, 2, 3]
print s.removeLeadingZeros(A)
A = [0, 0, 0, 1, 0, 2, 3]
print s.removeLeadingZeros(A)
