"""
https://www.interviewkickstart.com/problems/missing-numbers
"""
from re import I
from typing import List
def missingNumbers(input: List[int]) -> List[int]:
    N = len(input)+2    # Expected range
    expectedSum = sum(range(N+1))   # inclusive of last num
    actualSum = sum(input)
    print(expectedSum, actualSum)

    combinedSum = expectedSum - actualSum

    # Now sepearte them out using Average!
    average = combinedSum // 2
    
    actualAverageSum = 0
    for num in input:  # inclusive of average
        if num <= average:
            actualAverageSum += num
    expectedAverageSum = (average * (average+1)) // 2

    print(f"CombinedSum: {combinedSum}, average: {average}, actualAverageSum: {actualAverageSum}, expectedAverageSum: {expectedAverageSum}")

    firstNum = expectedAverageSum - actualAverageSum
    secondNum = combinedSum - firstNum
    return [firstNum, secondNum]

input = [6, 1, 3, 2]
print(missingNumbers(input))    # output [4,5]
input = [3,4,5]
print(missingNumbers(input))    # ouput [1,2 ]
input = [1, 2, 4]
print(missingNumbers(input))    # ouput [3, 5]

