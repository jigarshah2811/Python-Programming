"""
347. Top K Frequent Elements

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]

https://leetcode.com/problems/top-k-frequent-elements/
https://www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/
"""
class Solution(object):
    def Print_K_MostFrequent(self, arr, k):
        d = {}
        freq = {}

        for ele in arr:
            if ele in d:
                d[ele] += 1
            else:
                d[ele] = 1

        print "\nFrequency dictionary......"
        print d
        for key, val in d.items():
            try:
                freq[val].append(key)
            except:
                freq[val] = [1]

        print "Bucket elements according to Frequency...."
        print freq
        print "Most frequent {0} elements....".format(k)
        for index in reversed(xrange(len(freq.values()))):
            for ele in freq[index+1]:
                print ele,
                k -= 1
                if k <= 0:
                    return




s = Solution()
arr = [3, 1, 4, 4, 5, 2, 6, 1]
s.Print_K_MostFrequent(arr, 2)
arr = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
s.Print_K_MostFrequent(arr, 4)
