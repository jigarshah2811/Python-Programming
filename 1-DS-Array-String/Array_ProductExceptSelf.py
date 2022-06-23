"""
STRATEGY: Aux arrays, L & R to store product of all ele left side of ele, product of all ele right side of an ele
"""
class Solution(object):
    """
    https://leetcode.com/problems/product-of-array-except-self/
    """
    def productExceptSelf(self, nums):
        length = len(nums)
        # Edge cases
        if length == 0 or length == 1:
            # no values to multiply if n equals to 0 or 1
            return []


        # The left and right arrays as described in the algorithm
        L, R, answer = [0] * length, [0] * length, [0] * length

        # L[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the L[0] would be 1
        L[0] = 1
        for i in range(1, length):
            # L[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all
            # elements to the left of index 'i'
            L[i] = nums[i - 1] * L[i - 1]

        # R[i] contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R[length - 1] would be 1
        R[length - 1] = 1
        for i in reversed(list(range(length - 1))):
            # R[i + 1] already contains the product of elements to the right of 'i + 1'
            # Simply multiplying it with nums[i + 1] would give the product of all
            # elements to the right of index 'i'
            R[i] = nums[i + 1] * R[i + 1]

        # Constructing the answer array
        for i in range(length):
            # For the first element, R[i] would be product except self
            # For the last element of the array, product except self would be L[i]
            # Else, multiple product of all elements to the left and to the right
            answer[i] = L[i] * R[i]

        return answer


    """
    Approach 2: O(1) space approach
    Basically, we will be using the output array as one of L or R and we will be constructing the other one on the fly. 
    Let's look at the algorithm based on this idea.
    """
    def productExceptSelf_OptimizedSpace(self, nums):
        length = len(nums)
        productArr = [0] * length

        # LEFT: Product of all ele on LEFT of element
        leftProduct = 1
        for i in range(length):
            productArr[i] = leftProduct
            leftProduct = leftProduct * nums[i]

        # RIGHT: Product of all ele on RIGHT of element
        rightProduct = 1
        for i in reversed(list(range(length))):
            productArr[i] = productArr[i] * rightProduct
            rightProduct *= nums[i]

        return productArr

if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4]
    print(s.productExceptSelf(nums))
    print(s.productExceptSelf_OptimizedSpace(nums))

    nums = [4,5,1,8,2,10,6]
    print(s.productExceptSelf(nums))
    print(s.productExceptSelf_OptimizedSpace(nums))