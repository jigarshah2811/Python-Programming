"""
Length of the longest substring without repeating characters
https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

https://www.youtube.com/watch?v=sZosU8JjVaA

"""
class Solution(object):
    def MaxNonRepeatingSubSeq(self, str):
        # key: char, value: last index seen at
        seen = {}

        cur_len = max_len = 0
        start = end = 0

        for end in range(len(str)):
            if str[end] in seen:
                # seen before
                # New window starts....
                prev_index = seen[str[end]]
                start = max(start, prev_index + 1)
            # not seen before
            # current window extends
            seen[str[end]] = end
            max_len = max(max_len, end-start+1) # len of current NRS window
        return max_len


s = Solution()
print((s.MaxNonRepeatingSubSeq("GEEKSFORGEEKS") == 7))
print((s.MaxNonRepeatingSubSeq("abcabcbb") == 3))
print((s.MaxNonRepeatingSubSeq("bbbbbb") == 1))
print((s.MaxNonRepeatingSubSeq("pwwkew") == 3))