"""

Max contigous non-negative subarray
"""


def MaxContiguousNonNegativeSubArray(arr):
    INIT_VAL = 0
    result = []
    m = [INIT_VAL] * len(arr)
    m[0] = arr[0] if arr[0] > 0 else INIT_VAL

    for i in range(1, len(arr)):
        if arr[i] > INIT_VAL:
            m[i] = m[i-1] + arr[i]

    # Print subArray with Max
    if max(m) >= 0:
        maxIndex = m.index(max(m))
        while maxIndex >= 0 and m[maxIndex] != INIT_VAL:
            result.append(arr[maxIndex])
            maxIndex -= 1

    return result[::-1]


arr = [1, 2, 5, -7, 2, 5]
print(MaxContiguousNonNegativeSubArray(arr))
arr = [-1, -1, -1]
print(MaxContiguousNonNegativeSubArray(arr))
