"""
Given an array of integers write a function so that all the
even numbers are on the left side of the array and all the odd numbers are on the right side of the array.
"""


def ArrangeEvenOdd(A):
    Odd = 0
    for Even in xrange(len(A)):
        if A[Even] % 2 == 0:
            # Even Number, Swap with Odd number to go Left !
            save = A[Even]
            A[Even] = A[Odd]
            A[Odd] = save

            # Next swap with this Odd number
            Odd += 1
    return A

A = [2, 7, 3, 1, 9, 4]
print ArrangeEvenOdd(A)
A = [3, 7, 3, 1, 9, 4]
print ArrangeEvenOdd(A)
A = [2, 4, 6, 8, 9]
print ArrangeEvenOdd(A)
