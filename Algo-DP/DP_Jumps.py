board = [-1, 1, 1, 0, -2, 1, 1, 2, 0, -3, 1]
#index  [ 0, 1, 2, 3,  4, 5, 6, 7, 8,  9, 10]

d = dict()


def isSafe(index):
    if index < 0 or index > len(board) - 1:
        return False
    else:
        return True


"""
Method 1: Brute force, just add Jump value to index and see if we reach 0 for Win or continue!
"""


def canWin(index):
    nextIndex = index + board[index]

    # Continue till Win or Loose,
    while isSafe(nextIndex):
        # Win Condition: If we reached 0
        if board[nextIndex] == 0:
            return True
        else:

            # Prevent loop: Don't visit same index again!
            if d.__contains__(nextIndex):
                break
            else:
                # No win or loose yet

                # Mark this index is visited
                d[nextIndex] = board[nextIndex]
                # Try for next index!
                nextIndex += board[nextIndex]

    return False


"""
Method 1: DP  = BOTTOMS UP MEMOIZATION
Generate True/False for every index in array
    Start from one index (Visiting), Add Jump till we find 0 or go out of bound
    Loop: If we visit same index again, all chain is False
"""


def Recur(board, index):
    # Loose: Index going out of bound
    if not isSafe(index):
        d[index] = False
        return False
    # Win: Index reaches 0
    elif board[index] == 0:
        d[index] = True
        return True
    # Already in memory, solved index
    elif index in d and d[index] != "visited":
        return d[index]

    # Loose: Stuck in Loop
    elif index in d and d[index] == "visited":
        d[index] = False
        return False
    # Mark this index 'visited' and Recur for next index
    else:
        d[index] = "visited"
        retVal = Recur(board, index + board[index])
        d[index] = retVal
        return retVal


def IndexesCanWin(board):
    # Get True/False (Win/Loose) for all array indexes
    for index in range(len(board)):
        Recur(board, index)

IndexesCanWin(board)
print(d)
# print canWin(3)
# print canWin(4)




