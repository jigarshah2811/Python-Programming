"""
https://www.geeksforgeeks.org/decode-string-recursively-encoded-count-followed-substring/

Decode a string recursively encoded as count followed by substring
An encoded string (s) is given, the task is to decode it. The pattern in which the strings are encoded is as follows.

<count>[sub_str] ==> The substring 'sub_str'
                      appears count times.
Examples:

Input : str[] = "1[b]"
Output : b

Input : str[] = "2[ab]"
Output : abab

Input : str[] = "2[a2[b]]"
Output : abbabb

Input : str[] = "3[b2[ca]]"
Output : bcacabcacabcaca

"""


class Solution(object):
    def Decode(self, str):
        decodedStr = ""
        i = len(str)-1

        while i>=0:
            if str[i].isalpha():
                decodedStr += str[i]
            elif str[i].isdigit():
                decodedStr = self.multiTimes(decodedStr, ord(str[i])-ord('0'))
            i -= 1

        return decodedStr[::-1]


    def multiTimes(self, decodedStr, times):
        for i in range(times-1, 0, -1):
            decodedStr += decodedStr
        return decodedStr


s = Solution()
print(s.Decode("1[b]"))
print(s.Decode("2[ab]"))
print(s.Decode("2[a2[b]]"))
print(s.Decode("3[b2[ca]]"))