"""
http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.

Input: {-2, -3, 4, -1, -2, 1, 5, -3}
Output: Maximum contiguous sum is 7
Starting index 2
Ending index 6
"""


def maxSubArraySum(A):
    m = [-1]*len(A)
    m[0] = A[0]

    for i in range(1, len(A)):
        m[i] = max(m[i-1] + A[i], A[i])

    end = m.index(max(m))
    print("Max possible sum in array is {} ending at index {}".format(maxSum, end))
    return max(m), end


def maxSubArraySumNeg(A):
    m = [-1] * len(A)
    m[0] = A[0]

    for i in range(1, len(A)):
        if A[i] < 0:
            # Negative number
            m[i] = 0
            continue
        else:
            m[i] = m[i - 1] + A[i]

    # Find Indexes, Start and End from Array
    end = m.index(max(m))
    i = end
    while m[i] != A[i]:
        i -= 1
    start = i

    print("Max possible sum in array is {}\nArray=".format(max(m)))
    for i in range(start, end+1):
        print(A[i], end=' ')

    return max(m), start, end


"""
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
maxSum, start, end = maxSubArraySum(arr)
"""
arr = [1, 2, 5, -7, 2, 3]
maxSum, start, end = maxSubArraySumNeg(arr)
