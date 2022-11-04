from typing import List
import collections
import heapq

class Solution:
    """ DS: Freq Map  Algorithm: Bucket Sort
    FreqMap {num: times}
    Bucket  {times: [num1, num2, num3]}
    """
    def topKFrequent(self, nums: List[str], k: int) -> List[str]:
        # Create Freq Map # {num: times}
        freqMap = collections.defaultdict(int)
        for num in nums:
            freqMap[num] += 1
        print(freqMap)
        
        # Create FreqBucketMap # {times: [num1, num2, ...]}
        freqBucketMap = collections.defaultdict(list)
        for num, times in freqMap.items():
            freqBucketMap[times].append(num)
        print(freqBucketMap)
        
        # Now freqMap buckets stores all freq, we are interested in high to low times
        topFreqList = []
        for times in range(len(nums), -1, -1):      # <----- Descending order of "frequency"
            listOfWords = freqBucketMap[times]
            # Same freq words should be in sorted order!
            sortedWords = sorted(listOfWords)       
            topFreqList.extend(sortedWords)
        print(topFreqList)
        
        return topFreqList[:k]

def topKWords(words, k=1):
    freqMap = collections.defaultdict(int)
    maxHeap = []
    res = []

    for word in words:
        freqMap[word] += 1
    for word, freq in freqMap.items():
        heapq.heappush(maxHeap, (-freq, word))
    
    for i in range(k):
        (freq, word) = heapq.heappop(maxHeap)
        res.append(word)

    return res

words = ["i","love","leetcode","i","love","coding"]
res = topKWords(words, k=2)
print(res)

words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
res = topKWords(words, k=4)
print(res)