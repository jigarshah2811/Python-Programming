class Solution(object):
    def strstr(self, heystack, needle):
        for i in range(len(heystack) - len(needle) + 1):
            if heystack[i : i + len(needle)] == needle:
                return i
        return -1

if __name__ == "__main__":
    print(Solution().strstr("This is Simple string", "Simple"))
    print(Solution().strstr("This is Simple string", ""))

