def BubbleSort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            print("comparing ", arr[i], arr[j])
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                print(arr)
    
    return arr

def WRONG_BubbleSortEnumerate(arr: list) -> list:
    for i, num1 in enumerate(arr[:-1]):
        for k, num2 in enumerate(arr[i+1:]):        # Index j changes because it doesn't start from expected 0
            print("comparing ", num1, num2)
            if num1 > num2:
                arr[i], arr[j+1] = num2, num1
                print(arr)
    
    return arr


print(BubbleSort([3, 7, 4, 1]))
print(BubbleSort([5, 7, 6, 8, 3, 4, 2, 1]))

#print(WRONG_BubbleSortEnumerate(arr))

