"""
https://leetcode.com/problems/merge-sorted-array/
"""

""" Pattern: 2-Pointers         A [....ptr1] and B[... ptr2] merge on C[....ptr3]
            <------ Merge from Backwards! (High to Low nums)
"""
from typing import List


class Solution:
    def merge(self, A: List[int], lenA: int, B: List[int], lenB: int) -> None:
        i, j = lenA-1, lenB-1  # Merging array indexes
        
        k = lenA + lenB - 1    # resulting array index
        while i >= 0 and j >= 0:
            # Whatever is > we place it to the end of resulting array
            if A[i] >= B[j]:
                A[k] = A[i]     # pick A
                i -= 1
            else:
                A[k] = B[j]     # pick B
                j -= 1
            
            k -= 1              # Next element
        
        
        # Remaining elements from A and B where i and j are stuck at
        print(f"Remaining indexes A at: {i} and B at: {j}, result at: {k}")
        while i >= 0:
            A[k] = A[i]
            i -= 1
            k -= 1
        while j >= 0: 
            A[k] = B[j]
            j -= 1
            k -= 1
        
        
                