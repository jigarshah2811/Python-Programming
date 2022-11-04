import random
class Solution:
    def __init__(self, w: List[int]):
        # Generate [1/8, 3/8, 4/8]
        totalWeight = sum(w)
        for i, weight in enumerate(w):
            w[i] = weight / totalWeight
            
        # Generate on number line for uniform distribtion betwee 0%-100%
        # [1/8, 4/8, 1]     See last weight will always be 1 (=100%)
        for i, weight in enumerate(w):
            if i == 0:  # skip 1st
                continue
            w[i] += w[i-1]
        
        self.w = w

    def pickIndex_orderN(self) -> int:
        # Generate a random uniformity between 0...1
        pickedWeight = random.uniform(0, 1)
        
        for i, weight in enumerate(self.w):
            if pickedWeight <= weight:
                return i
    
    
    """ Pattern: Binary Search  ---- Get Index of value between (0, ..., 1)
    If the value does not exists, return index of closest value target=0.26 in [0.1, 0.25, 0.75] would return index=1
    """
    def pickIndex_BinarySearch(self):
        target = random.uniform(0, 1)
        # print(f"target: {target}")
        
        # Make it unform by selecting the index based on probability weight
        low, high = 0, len(self.weights)-1
        
        while low < high:
            mid = (low + high) >> 1
            # print(f"mid: {mid}, val: {self.weights[mid]}")
            if self.weights[mid] == target:
                return mid

            if target > self.weights[mid]:
                # print(f"Searching on R ---> ")
                low = mid + 1
            else:
                # print(f"Searching on L <----")
                high = mid
        
        # At this point low and high would be same
        return min(low, high)