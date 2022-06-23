"""
STRATEGY: Map, Modify as you go...
"""
class Solution(object):
    """
    https://www.geeksforgeeks.org/sieve-of-eratosthenes/
    """
    def countPrimes(self, n):
        # Edge case
        if n < 3:
            return 0

        # Create a table of all numbers are prime: True
        prime = [True for i in range(n)]
        prime[0] = prime[1] = False

        # Iterate through each number in table starting from 1st prime number=2
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                # Mark all multiplication... prime=False!
                # Start with 2*2 and mark all increments of 2
                # Start with 3*3 and mark all increments of 3
                # Start with 5*5 and mark all increments of 5
                for p in range(i*i, n, i):
                    prime[p] = False

        return sum(prime)


    def firstNonRepeatingNum(self, nums):
        from sys import maxsize
        d = {}

        # Build a freq map but also store index
        # {Num --> (freq, index)}
        for i, num in enumerate(nums):
            if num in d:
                d[num] = (d[num][0]+1, i)
            else:
                d[num] = (1, i)

        print(d)

        # Walk through dict key to find num with freq=1 and with min index
        resIndex = maxint
        for num, (freq, index) in list(d.items()):    # OPTIMIZE: Iterate only on keys not the entire nums array again!!!
            if freq == 1: # Non repeating number
                resIndex = min(resIndex, index) # First non repeating number

        print(resIndex)
        return nums[resIndex] if resIndex == maxint else -1


s = Solution()
nums = [0,1,0,3,12]
#print ("Total prime numbers till value: {0}, are: {1}".format(50, s.countPrimes(50)))
#print ("Total prime numbers till value: {0}, are: {1}".format(50, s.countPrimes(9999999)))

nums = [3,4,1,2,5,2,1,4,2]  # 3 and 5 don't repeat, so return 3
print(("First non repeating number is: ", s.firstNonRepeatingNum(nums)))