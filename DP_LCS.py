"""
http://www.geeksforgeeks.org/dynamic-programming-set-4-longest-common-subsequence/
"""


def LCS(str1, str2):
    m = len(str1)
    n = len(str2)
    L = [[0]*50]*50

    for i in xrange(len(str1)+1):
        for j in xrange(len(str2)+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                L[i][j] = 1 + L[i-1][j-1]
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    print L[m][n]


str1 = "ABCDGH"
str2 = "AEDFHR"
LCS(str1, str2)