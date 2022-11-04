class Solution:
    def __init__(self):
        pass

    def printString(self, n):

        for i in range(1, n+1):

            # Check divisible for BOTH 4 and 6
            if (i % 4) == 0 and (i % 6) == 0:
                print("Hello PaloAlto Networks")
            
            # Check divisible by 4
            elif (i % 4) == 0:
                print("PaloAlto")

            # Check divisible by 6
            elif (i % 6) == 0:
                print("Networks")

            
s = Solution()
print(s.printString(100))
print(s.printString(0))
