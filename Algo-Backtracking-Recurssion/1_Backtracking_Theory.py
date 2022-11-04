"""
 Backtracking works in an incremental way to attack problems.
Typically, we start from an empty solution vector and one by one add items
(Meaning of item varies from problem to problem. In context of Knight’s tour problem, an item is a Knight’s move).

When we add an item, we check if adding the current item violates the problem constraint,
if it does then we remove the item and try other alternatives.
If none of the alternatives work out then we go to previous stage and remove the item added in the previous stage.
If we reach the initial stage back then we say that no solution exists. If adding an item doesn’t violate constraints
then we recursively add items one by one. If the solution vector becomes complete then we print the solution.
"""

"""
https://leetcode.com/problems/palindrome-permutation-ii/discuss/69717/Backtrack-Summary%3A-General-Solution-for-10-Questions!!!!!!!!-Python-(Combination-Sum-Subsets-Permutation-Palindrome)
"""
