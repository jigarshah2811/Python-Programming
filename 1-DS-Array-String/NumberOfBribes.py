"""
https://www.hackerrank.com/challenges/new-year-chaos/leaderboard?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""
class Solution:
    def numberOfBribes(self, maxBribe, arr):
        numBribes = 0

        for i in range(len(arr)):

            curPosition = arr[i] - (i+1)
            if curPosition > 0:
                print(("Bribing guy: {0}, numBribes: {1}".format(arr[i], curPosition)))
                # The person is ahead of it's original position, by bribing
                numBribes += curPosition

        print(numBribes)
        if numBribes > maxBribe:
            print("Too chaotic")





s = Solution()
personsQueue = [2,1,5,3,4]
numBribes = s.numberOfBribes(2, personsQueue)
