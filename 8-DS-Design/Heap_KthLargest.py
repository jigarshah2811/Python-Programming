import heapq


class k(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        heapq.heapify(nums)
        print(nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        pass

# Your k object will be instantiated and called as such:
# obj = k(k, nums)
# param_1 = obj.add(val)


k = k(3, [4,5,8,2])
print((k.add(3)))
print((k.add(5)))
print((k.add(10)))
print((k.add(9)))
print((k.add(4)))
