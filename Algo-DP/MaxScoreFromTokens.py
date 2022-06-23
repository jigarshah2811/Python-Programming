"""
Bag of tokens

Trick: # Trading (min)tokens to increase score, trading score to increase (max)tokens
"""


"""
https://leetcode.com/articles/bag-of-tokens/

You have an initial power P, an initial score of 0 points, and a bag of tokens.

Each token can be used at most once, has a value token[i], and has potentially two ways to use it.

If we have at least token[i] power, we may play the token face up, losing token[i] power, and gaining 1 point.
If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.
Return the largest number of points we can have after playing any number of tokens.

 

Example 1:

Input: tokens = [100], P = 50
Output: 0
Example 2:

Input: tokens = [100,200], P = 150
Output: 1
Example 3:

Input: tokens = [100,200,300,400], P = 200
Output: 2
 

Note:

tokens.length <= 1000
0 <= tokens[i] < 10000
0 <= P < 10000
"""
class Solution(object):
    def __init__(self):
        pass

    def bagOfTokens(self, tokens, P):
        score, maxScore = 0, 0

        tokens = sorted(tokens)
        minPointer = 0
        maxPointer = len(tokens)-1

        print(tokens, minPointer, maxPointer)
        while minPointer <= maxPointer:
            # 1) GiveUp minToken and increase score
            if tokens[minPointer] <= P:
                P = P - tokens[minPointer]
                minPointer += 1
                score += 1

            # 2) GiveUp score for increasing maxToken
            elif score > 0:
                score -= 1
                P = P + tokens[maxPointer]
                maxPointer -= 1

            else:
                break

            maxScore = max(maxScore, score)

        return maxScore



s = Solution()

# Not enough P to start with
tokens = [100]
assert(s.bagOfTokens(tokens, 50) == 0)

# Trading (min) tokens to increase score, No trading of score
tokens = [100, 200]
assert(s.bagOfTokens(tokens, 150) == 1)

# Trading (min)tokens to increase score, trading score to increase (max)tokens
tokens = [400, 100, 300, 200]
assert(s.bagOfTokens(tokens, 200) == 2)

