N = 5
m = [[0] * N for i in xrange(N)]
m[0][1], m[0][2] = 1, 1

m = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
    ]
print m


def isSafe(row, col):
    if 0 <= row <= N-1 and 0 <= col <= N-1 and m[row][col] == 1:
        return True
    else:
        return False


def Recur_Mark_Island(row, col):
    global m
    # If the cell is within boundaries and not yet visited
    if isSafe(row, col):
        # Mark Visited
        m[row][col] = 0

        # Mark all neighbour islands visited
        Recur_Mark_Island(row + 1, col)
        Recur_Mark_Island(row - 1, col)
        Recur_Mark_Island(row, col + 1)
        Recur_Mark_Island(row, col - 1)
        Recur_Mark_Island(row + 1, col + 1)
        Recur_Mark_Island(row + 1, col - 1)
        Recur_Mark_Island(row - 1, col + 1)
        Recur_Mark_Island(row - 1, col - 1)


numIslands = 0
for row in xrange(N):
    for col in xrange(N):
        # If an Island is yet to be visited!
        if m[row][col] == 1:
            # Visit island, count
            numIslands += 1
            # Mark all Connected Island Visited recursively in all directions to eliminate re-count
            Recur_Mark_Island(row, col)


print numIslands

