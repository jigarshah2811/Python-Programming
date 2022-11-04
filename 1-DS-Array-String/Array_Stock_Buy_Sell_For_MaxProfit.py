"""
STRATEGY: Sliding window (Find localMin, localMax and txn.... Keep going)
"""
"""
https://www.geeksforgeeks.org/stock-buy-sell/
Stock Buy Sell to Maximize Profit
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling in those days. For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.
"""

"""
Solution:
If we are allowed to buy and sell only once, then we can use following algorithm. Maximum difference between two elements. Here we are allowed to buy and sell multiple times. Following is algorithm for this problem.
1. Find the local minima and store it as starting index. If not exists, return.
2. Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
3. Update the solution (Increment count of buy sell pairs)
4. Repeat the above steps if end is not reached.
"""
class Solution(object):
    def maxProfitOnce(self, price):
        minPrice = maxint
        maxProfit = 0

        i = 0
        while i < len(price):
            minPrice = min(price[i], minPrice)
            maxProfit = max(price[i]-minPrice, maxProfit)
            i+=1

        return maxProfit

    def maxProfitOnce(self, price):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf')
        maxPrice = -float('inf')
        maxProfit = -float('inf')

        i = 0
        while i < len(price):

            # Find MinPrice (For current sliding window)
            while i < len(price) - 1 and price[i] <= minPrice:
                minPrice = price[i]
                i += 1

            # Find MaxPrice (For current sliding window)
            j = i
            while j < len(price) and price[j] >= maxPrice:
                maxPrice = price[j]
                j += 1
            i = j

            # Txn: HISAB (For current sliding window)
            if maxPrice > minPrice:
                print(("Buy at: {0}, Sell at: {1}".format(minPrice, maxPrice)))
                maxProfit += maxPrice - minPrice
                # Reset (To find Next sliding window)
                minPrice = float('inf')
                maxPrice = -float('inf')

        return maxProfit



s = Solution()
print("Max Profit:{0}".format(s.maxProfitOnce([1,2,3,4,5])))
print("Max Profit:{0}".format(s.maxProfitOnce([5,4,3,2,1])))
print("Max Profit:{0}".format((s.maxProfitOnce([100, 180, 260, 310, 40, 535, 695]))))
print("Max Profit:{0}".format(s.maxProfitOnce([7,1,5,3,6,4])))
print("Max Profit:{0}".format(s.maxProfitOnce([7,6,4,3,1])))
#print "Max Profit:{0}".format(s.maxProfitOnce([7,1,5,3,6,4]))


"""Also Look at 
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
"""