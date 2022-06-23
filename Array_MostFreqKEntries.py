"""

a = ["hi", "hello", "query", "hello", "hi"]
k = 2

O(n)
d = {
    "hi": 3
    "hello": 2
    "query": 1
}

freq_arr = []

O(nlogn)

push: Log(n)
pop: log(n)

O(height)

comparator operator(p, q) {
    if p[freq] > q[freq]:
        return p
}

priority_Queue:
Max priority (query)
lower priority(query)

while k > 0:
    pq.pop()
    k -= 1

result => [frequency, list of queryes]
result = {frequency, listOfQueries}
    1: "query"
    2: ["hello", "hi"]
    3: []
    ...
    1000: ["hello"]
]


output = ["hi", "hello"]

most frequent k query?

"""



class Solution(object):
    def printKMostFreq(self, arr, k):
        d = {}
        # Frequency
        for query in arr:
            if query in d:
                d[query] += 1
            else:
                d[query] = 1

        print  "Lets look at d:"
        print d

        # Create a frequency dict with [freq, [list of wueryes]]
        freq_queries = {}
        for queryString, freq in d.items():
            if freq not in freq_queries:
                freq_queries[freq] = [queryString]
            else:
                freq_queries[freq].append(queryString)

        print "Lets look at freq_queries:"
        print freq_queries

        result = []
        # Now traverse backward and print k ele
        for freq in xrange(len(arr), 0, -1):
            if freq in freq_queries:
                for queryString in freq_queries[freq]:
                    result.append(queryString)

        return result[:k]




s = Solution()
queries = ["hi", "hello", "hello", "hi", "query"]
k = 3
result = s.printKMostFreq(queries, k)
print "{0} most frequent strings are: {1}".format(k, result)