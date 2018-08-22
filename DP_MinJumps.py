"""
http://www.geeksforgeeks.org/minimum-number-of-jumps-to-reach-end-of-a-given-array/

QUE: Minimum number of jumps to reach end
Given an array of integers where each element represents the max number of steps that can be made forward from that element. Write a function to return the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then cannot move through that element.

Example:

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 ->9)
First element is 1, so can only go to 3. Second element is 3, so can make at most 3 steps eg to 5 or 8 or 9.

"""

jumps = 1


def minJumps(arr, low, high):
    global jumps
    if low >= high:
        return

    i = low
    temp = []
    tempIndex = 0
    while i < (low + arr[low]) and i < high:
        # Check next steps possible

        # Constraint 1: If the ele(steps) is > steps remaining
        if arr[i] < high - i:
            temp.append(arr[i])
            tempIndex += 1
        i += 1

    # Constraint 2: Min amongst all to reach to the end
    if temp is not []:
        jumps += 1
        minJumps(arr, temp.index(min(temp)), high)
    return


arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
minJumps(arr, 1, len(arr)-1)
print jumps
