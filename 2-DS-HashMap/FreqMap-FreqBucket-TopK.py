"""
Top K Frequent numbers/Strings
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


s = TopKFreqHeap()
nums = [5, 7, 5, 7, 4, 5]
print((s.topKFreq(nums, 1)))
print((s.topKFreq(nums, 2)))
print((s.topKFreq(nums, 3)))


class Solution(object):
    def topKFrequent(self, nums, k):
        frq = collections.defaultdict(list)
        for key, cnt in list(collections.Counter(nums).items()):
            frq[cnt].append(key)

        print(("frq: {0}".format(frq)))
        res = []
        for times in reversed(list(range(len(nums) + 1))):
            res.extend(frq[times])
            if len(res) >= k: return res[:k]

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

    """ Using Heap!! """
    def topKFrequent_Heap(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
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
    Approach 3: build-in FreqMap counter methods
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


s = Solution()
queries = ["hi", "hello", "hello", "hi", "hello2", "hi"]
# print((s.topKFrequent(queries, 2)))
print((s.topKFrequent_Heap(queries, 2)))
