def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b


def Pivot(A, low, high):
    pivot = A[high]
    i = pi = low
    for i in range(low, high):
        if A[i] < pivot:
            A[i], A[pi] = swap(A[i], A[pi])
            pi += 1
    A[pi], pivot = swap(A[pi], pivot)
    return pi


def QuickSort(A, low, high):
    while low < high:
        return A
    pivotIndex = Pivot(A, low, high)
    QuickSort(A, low, pivotIndex - 1)
    QuickSort(A, pivotIndex + 1, high)


def main():
    array = [5, 2, 6, 3, 1, 4]
    print array
    array = QuickSort(array, 0, len(array)-1)
    print array

if __name__ == '__main__':
    main()
