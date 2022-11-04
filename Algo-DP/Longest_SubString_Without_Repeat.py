"""
  Longest Substring Without Repeating Characters

https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/779/
https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/
"""

def longestUniqueSubStr(str):
    # HashMap {Char --> IndexLastSeen}
    d = dict()

    cur_len = 0        # To store the length of current substring
    max_len = 0        # To store the result

    # Start from the second character. First character is already
    # processed (cur_len and max_len are initialized as 1, and
    # visited[str[0]] is set
    for i in range(len(str)):

        # Char not seen or seen but not part of Current SubString
        # If the currentt character is not present in the already
        # processed substring or it is not part of the current NRCS,
        # then do cur_len++
        if str[i] not in d or i - cur_len > d[str[i]]:
            cur_len += 1
        else:
            # Char seen in current Substring
            # Also, when we are changing the NRCS, we should also
            # check whether length of the previous NRCS was greater
            # than max_len or not.
            max_len = max(cur_len, max_len)
            cur_len = i - d[str[i]]

        # update the index of current character
        d[str[i]] = i

    # Compare the length of last NRCS with max_len and update
    # max_len if needed
    max_len = max(cur_len, max_len)
    return max_len




print(longestUniqueSubStr("GEEKSFORGEEKS"))
print(longestUniqueSubStr("LEETCODE"))