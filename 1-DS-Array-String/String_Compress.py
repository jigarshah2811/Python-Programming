"""
https://nbviewer.org/github/donnemartin/interactive-coding-challenges/blob/master/arrays_strings/compress/compress_challenge.ipynb

Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'. Only compress the string if it saves space.

"""
import unittest


class TestSolution(unittest.TestCase):
    def testCompressString(self, func):
        self.assertEqual(func(""), "")
        self.assertEqual(func("ABC"), "ABC")
        self.assertEqual(func("AAABC"), "A3BC")
        self.assertEqual(func("AAABCCCC"), "A3BC4")


class Solution:
    def compressString(self, inputStr: str) -> str:
        """
        Pattern: If the prior char is same as this char - DUP - just increment count
                 No Dup - embed the last char and counter
        """
        # Edge case, where string has <2 char "" "A" - no compression needed
        if len(inputStr) < 2:
            return inputStr

        # Deal with lists not str (immutable)
        res, s = list(), list(inputStr)

        counter = 1     # Default counter for a new char
        # Embed first char as-is, then count total occurances of this char to embed in last
        res.append(s[0])

        for i in range(1, len(s)):
            if s[i] == s[i-1]:  # DUP, just increment counter and append at the last
                counter += 1
            else:               # New char, append counter for prior char and append new char
                if counter > 1:
                    res.append(counter)
                    counter = 1
                res.append(s[i])

        if counter > 1:
            res.append(counter)

        return ''.join(map(str, res))


def main():
    solution = Solution()

    testSolution = TestSolution()
    testSolution.testCompressString(solution.compressString)


if __name__ == "__main__":
    main()
