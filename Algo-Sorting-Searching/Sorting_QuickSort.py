def QuickSort(arr: list) -> list:
    return QuickSortRecursive(arr, 0, len(arr) - 1)

def QuickSortRecursive(arr: list, start: int, end: int) -> list:
    """
    QuickSort is like Tree Pre-order traversal
        -   Sort elements (Partition Index), final place for pivot
        -   Recur for L sub-array
        -   Recur for R sub-array
    """
    # Base case
    if start < end:
        print(f"Partition: {start} <--> {end}")
        pi = Partition(arr, start, end)

        # The pi indicates SPLIT of the array, pi has right final elemenet
        # Repeat same process to sort L and R sub-arrays
        QuickSortRecursive(arr, start, pi-1)
        QuickSortRecursive(arr, pi+1, end)

    return arr

def Partition(arr: list, start: int, end: int) -> int:
    # Single pass
    pivot, pi = arr[end], start

    print(f"Pivot: {pivot}")
    for i in range(start, end):
        # Compare with pivot, all values less then pivot are swapped and partition index is moved
        if arr[i] < pivot:
            arr[i], arr[pi] = arr[pi], arr[i]
            pi += 1
    
    # At the end of single pass -> "pi" points to the final location pivot should be at
    arr[pi], arr[end] = arr[end], arr[pi]
    return pi

#print(QuickSort([2, 1, 0, 5, 4, 3]))
#print(QuickSort([]))
print(QuickSort([5, 7, 8, 6, 3, 4, 2, 1]))

