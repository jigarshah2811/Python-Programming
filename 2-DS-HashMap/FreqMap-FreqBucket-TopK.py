""" Q: Top K Frequent numbers/Strings

DS: FreqMap and FreqBucket (Pattern: Bucket Sort)
DS: Counter                (Pattern: Built in method most_common() on Python Dict!)
DS: MinHeap                (Pattern: (freq, num) in minHeap, remove (N-K) min freqs)
DS: MinHeap                (Pattern: (freq, num) size:K minHeap, keep removing exessive min freq leaving top K freq starting (minFreq, num) to (maxFreq, num))
DS: MaxHeap                (Pattern: (-freq, num) in maxHeap, first entry will be highest freq and descending order)
DS: MaxHeap                (Pattern: (-freq, num) size: K maxHeap, keep removing last entry if less then new entry.)
"""
import collections
import heapq
class TopKFreqHeap:
    def __init__(self):
        self.freqMap = collections.Counter()  # HasMap {Ele -> Freq}
        self.freqBucket = collections.defaultdict(list)  # HashMap {Freq -> List of Ele}
        self.maxFreq = 0

    def push(self, ele):
        self.freqMap[ele] += 1  # Update freqMap
        f = self.freqMap[ele]

        self.freqBucket[f].append(ele)  # Update freqBucketList
        self.maxFreq = max(f, self.maxFreq)

    def pop(self):
        ele = self.freqBucket[self.maxFreq].pop()  # Get most freq ele
        self.freqMap[ele] -= 1

        if not self.freqBucket[self.maxFreq]:  # MaxFreq bucket is now empty
            self.maxFreq -= 1

        return ele

    def topKFreq(self, nums, k):
        for ele in nums:
            s.push(ele)

        print(("freqBucket: {0}".format(self.freqBucket)))
        res = []
        for i in range(k):
            res.append(s.pop())
        return res


# s = TopKFreqHeap()
# nums = [5, 7, 5, 7, 4, 5]
# print((s.topKFreq(nums, 1)))
# print((s.topKFreq(nums, 2)))
# print((s.topKFreq(nums, 3)))


class Solution(object):
    """ Using FreqMap and FreqBucket (Bucket Sort)"""
    def topKFrequentWords_FreqMap(self, words, k):
        # Step 1) Create Freq Map  {word: count}
        freq = collections.defaultdict(int)
        maxCount = 0
        for word in words:
            freq[word] += 1
            maxCount = max(maxCount, freq[word])
        print(freq)

        # Step 2) Sort by Freq (Bucket Sort)
        buckets = [[] for i in range(maxCount+1)]
        for word, count in freq.items():
            buckets[count].append(word)
 
        print(buckets)

        # Step 3) Traverse from reverse to find the ones with most count
        res = []
        for i in range(maxCount, -1, -1):
            res.extend(buckets[i])

        return res[:k]

    def topKFrequent1(self, arr, k):
        # Create a freq Map
        d = collections.Counter(arr)
        print(("freq map: {0}".format(d)))

        # Create buckets of freq. Bucket[Freq] = list(item1, item2)
        freqList = collections.defaultdict(list)
        for query, freq in list(d.items()):
            freqList[freq].append(query)
        print(("freq List: {0}".format(freqList)))

        # Now traverse backward and print k ele
        result = list()
        for freq in reversed(list(freqList.keys())):
            query = freqList[freq].pop()
            result.append(query)

        return result[:k]

    """ 
    DS: MinHeap!!  Pattern: Store freq of nums, remove first (N-K) small freq leaving TOP K freq numbers
    """
    def topKFrequent_Heap(self, nums, k):
        freqMap = collections.defaultdict(int)
        for i, num in enumerate(nums):
            freqMap[num] += 1

        # Create heapq of K items       --> Element ( Key, Freq ) .... This will be sorted by Freq
        q = []
        for key, freq in list(freqMap.items()):
            heapq.heappush(q, [freq, key])
        heapq.heapify(q)
        print(q)

        # Now the minFreq elements are at top of Heap. So remove everything but K
        for i in range(len(q)-k):
            tmp = heapq.heappop(q)        # Discard min freq elements, Keep K more freq

        # Now all Top K Freq are on heap
        topkResult = []
        for i in range(k):
            topkResult.append(heapq.heappop(q)[1])
        return topkResult
        # return heapq.nlargest(k, count.keys(), key=count.get)

    """ 
    DS: MinHeap!!  Pattern: K size Heap!
    Pattern: Keep storing (freq, num), keep size K by removing excess MIN (freq, num) leaving K entries
    (lowestFreq, num) will be on top so give result from reverse heap[::-1]
    """
    def topKFrequent_MinHeapKSize(self, nums, k):
        # Step 1) Create Freq Map
        freqMap = collections.defaultdict(int)
        for word in words:
            freqMap[word] += 1

        # Step 2) Heap Sort: using MAXHEAP: (-freq, word) so highest freq will be on top
        minHeap = []
        for word, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, word))    # MAXHEAP
            while len(minHeap) > k:
                heapq.heappop(minHeap)     # Remove LOWER elements

        # Step 3) MinHeap has values in ASCENDING order so capture TOP K from reverse
        res = []
        for _, (freq, word) in enumerate(minHeap[::-1]):
            res.append(word)
        return res

    """ 
    DS: MaxHeap!!  Pattern: Store (-1*Freq, Num) in Heap, 
    Multiply with (-1) will keep the HIGEST Frequency numbers on Top
    """
    def topKFrequent_Heap(self, nums, k):
        # Step 1) Create Freq Map
        freqMap = collections.defaultdict(int)
        for word in words:
            freqMap[word] += 1

        # Step 2) Heap Sort: using MAXHEAP: (-freq, word) so highest freq will be on top
        maxHeap = []
        for word, freq in freqMap.items():
            heapq.heappush(maxHeap, (freq*-1, word))    # MAXHEAP

        # Step 3) get the TOP K from MAXHEAP
        res = []
        for i in range(k):
            (freq, word) = heapq.heappop(maxHeap)
            res.append(word)

        return res


    """
    Approach 3: build-in FreqMap counter methods -- TOP K in MAP!
    """
    def topKFrequent_Counter(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # nums=[1,1,1,2,2,3], k=2
        c = collections.Counter(nums)  # Counter({1: 3, 2: 2, 3: 1})
        k_most_common = c.most_common(k)  # [(1, 3), (2, 2)]
        return [element for element, count in k_most_common]  # [1, 2]


# s = Solution()
# queries = ["hi", "hello", "hello", "hi", "hello2", "hi"]
# # print((s.topKFrequent(queries, 2)))
# print((s.topKFrequent_Heap(queries, 2)))

s = Solution()
words = ["i", "love", "leetcode", "love", "i"]
print(s.topKFrequentWords_FreqMap(words, 1))
print(s.topKFrequentWords_FreqMap(words, 2))
print(s.topKFrequentWords_FreqMap(words, 3))


words = ["i", "love", "leetcode", "love", "i"]
print(s.topKFrequent_MinHeapKSize(words, 1))
print(s.topKFrequent_MinHeapKSize(words, 2))
print(s.topKFrequent_MinHeapKSize(words, 3))