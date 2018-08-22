class Solution(object):
    def largestSquareInMatrix(self, input):
        globalMax = -1
        rows = len(input)
        cols = len(input[0])
        output = [[0 for row in xrange(rows)]for col in xrange(cols)]

        print rows, cols

        for row in xrange(rows):
            for col in xrange(cols):
                # As-is. No reuse for 1st row and 1st col.
                if row == 0 or col == 0:
                    output[row][col] = input[row][col]

                # If value is 0, ignore
                if input[row][col] == 0:
                    output[row][col] = 0
                # If value is 1, consider min from prior row, col, diagonal
                else:
                    print row, col
                    output[row][col] = min(output[row-1][col],
                                           output[row][col-1],
                                           output[row][col]) + 1
                    print output[row][col]
                    globalMax = max(output[row][col], globalMax)

        print output
        return globalMax


rows = cols = 5
input = [[0, 1, 1, 0, 1], [1, 0, 0, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 0], [0, 1, 1, 1, 1]]
print "Input..."
print input
s = Solution()
print s.largestSquareInMatrix(input)
