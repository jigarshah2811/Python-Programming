class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        vows = set('aeiouAEIOU')
        l, r = 0, len(s) - 1
        while l <= r:
            while l <= r and s[l] not in vows: l += 1
            while l <= r and s[r] not in vows: r -= 1
            if l > r: break
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        return ''.join(s)

    def reverseVowels1(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set('aeiouAEIOU')
        s = list(s)

        # Two pointers
        low, high = 0, len(s) - 1

        while low < high:
            while low < high and s[low] not in vowels:
                low += 1

            while low < high and s[high] not in vowels:
                high -= 1

            if low > high: break
            s[low], s[high] = s[high], s[low]

            low, high = low + 1, high - 1

        return ''.join(s)

sol = Solution()
print((sol.reverseVowels1("hello")))
