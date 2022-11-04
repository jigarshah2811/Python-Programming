""""""




"""======================      2ND TELEPHONIC INTERVIEW ============================"""

""" The input string can contain letters too : "()(a)()" "()(.)"

Input: "()())()" -- "{{{]]]]}}}"
Output: "()()()"

Input: "((()))"
Output:  "((()))"

Input: ")()"
Input: "()"

Input: "(()))"

"()())()"

"((((()"
i == ==

"(((("
""

"(()))()"
"(())()"

"()()"

"(())"

"()"
"""

# def backtrack(s, left, right, rem_left, rem_right):
#     # Base condition
#     if i == len(s) - 1:
#         if rem_left == 0 and rem_right == 0:
#             if checkIfValid(expr):
#                 return expr
#     else:
#
#         if (s[i] == "(" and rem_left > 0)
#             backtrack(s, i + 1, left, right, rem_left - 1, rem_right)
#         elif (s[i] == ")" and rem_right > 0):
#             backtrack(s, i + 1, left, right, rem_left, rem_right - 1)
#
#             # We generate valid express
#         expr += s[i]
#
#         if not "(" or not ")"
#             backtrack(s, i + 1, left, right, rem_left, rem_right)
#
#         if s[i] == "(":
#             backtrack(s, i + 1, left + 1, right, rem_left, rem_right)
#         else:
#             left > right and s[i] == ")"
#         backtrack(s, i + 1, left, right + 1, rem_left, rem_right)
#
#     expr.pop() # Backtrack
#
#
# def removePar(self, s):
#     # Count total ( and count total )
#     for ch in s:
#         if ch != "(" or ch != ")":
#             continue
#         elif ch == "(":
#             left += 1
#         else:
#             right += 1 if left == 0 else right
#             left = left - 1 if left > 0 else left
#
#     self.backtrack(s, 0, 0, left, right)
#     return res
#
#
# """ Iterative solution using stack """
# Stack:
# ""
# res = "("
#
# res = ""
# for char in input:
#     if char:
# res += char
# continue
#
# elif "(":
# s.push("(")
# res +
# else:
# if not s.isempty() and s.peek() == "(":
#     res += s.pop()
#     res += ")"
# else:
#     continue
#
# return res