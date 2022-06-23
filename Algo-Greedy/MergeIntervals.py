# SNOWFLAKES INTERVIEW
# 
# Your previous Plain Text content is preserved below:
#
# This is just a simple shared plaintext pad, with no execution capabilities.
#
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
#
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/settings
#
# Enjoy your interview!
#
#
# Hello... Jigar Here
#
#
#
#  (3, 3)
#
# //
# //  [(1,3),(2,6),(7,10)]  # VALID
#
# res : (1, 6), (7. 10)
#
# Find What needs to be merged
#
# Overlapping...
#
# if cur.start < prev.End
#
#    ---   PRE
#     ---  CUR
#
#   (2, 6) (6, 10)
# (2, 10)

#   1 2 3 4 5 6 7 8 9 10....
#
#
#     Ex2:  [(2,6),(7,10) (1,3)]  # INVALID
#
# //    -> [(1,6),(7,10)]  OUTPUT ?
#
#
#

class Solution():
    def merge(self, intervals):

        # Edge case
        if len(intervals) == 0:
            return []

        res = []
        start, end = 0, 1

        for i, cur in enumerate(intervals):
            if i == 0:
                res.append(cur)
                continue

            pre = res[-1]

            if cur[start] <= pre[end]:  # Overlapping
                # UPDATE
                res[-1][end] = max(pre[end], cur[end])

            else:  # NOT OVERLAPPING
                # ADD
                res.append(cur)

        return res


s = Solution()
intervals = [(1, 3), (2, 6), (7, 10)]

print(s.merge(intervals))

#
# add(i,j) - add an interval to the working set
# check(v) - returns true if value is contained in the working set
#

# add(1,3)
# check(4) -> false
# add(2,6)
# check(4) -> true
"""

LOCKS(R / W
locks)

PERSISTENT == == EXT
DB....Caching...Write - throught
cache, writeb - ack
cache...

CAP == == = > CONSISTENCY
OR
AVAILABILITY

ADD: Make
sure
overlapping
merge...Gureentreed
always
SORTED...

(1, 6)

Check: BINARY
SEARCH....start....index: Mid...walk and see if entire
ranges
exists

SCALE: DISTRIBUTE
RANGE(1 - 100)
M1(101 - 200)
M2.....CONSISTENT
HASHING(DYNAMIC)
LOAD - BALANCING... + HA(REMAP
keys
belongs
machine
went
down)
"""

#    1
#   / \
#  2   3      toDelete = {1, 3}     CHECK: L & R add in result
# / \ / \
# 4  5 6  7   -> [(1), (6), (7)] ==== ROOTS of DETACHED TREES
class Solution():

    def postOrder(root):
        if root is None:  # None can't be deleted
            return None

        # L R then C
        root.left = postOrder(root.left)
        root.right = postOrder(root.right)

        if root.val in toDelete:
            # LEAF/ 1 child/ 2child
            if root.left:
                res.append(root.left)  # This is new TREE
            if root.right:
                res.append(root.right)  # this is new tree

            return None

        else:

            return root

    res = []
    postOrder(root)
    return res