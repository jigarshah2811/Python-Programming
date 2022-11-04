class Solution:
    def mainFun(self):
        def subFun():
            res.append(1)
            return

        res = []
        subFun()
        print(res)

s = Solution()
s.mainFun()
