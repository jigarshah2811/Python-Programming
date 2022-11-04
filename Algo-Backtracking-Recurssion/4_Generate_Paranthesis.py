"""
######### ------- BACKTRACKING -----------#########

Visual explanation: https://leetcode.com/problems/generate-parentheses/solution/

"""


class Solution:
    def generateParenthesis(self, n):
        def backtrack(sol, left, right):
            # 1) Base case: If a solution is found
            if len(sol) >= n*2:   # String size is left+right
                result.append(sol)
                return True

            # 2) Breath! ---> All possible moves, consume left or right paran available
            # 3) isSafe --> Constraint: We are taking care using left & right
            if left > 0:  # Consume left
                sol += "("
                backtrack(sol, left - 1, right)
                sol = sol[:-1]

            if right > left:
                sol += ")"
                backtrack(sol, left, right - 1)
                sol = sol[:-1]

        result = []
        backtrack(sol="", left=n, right=n)
        return result


s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(5))
