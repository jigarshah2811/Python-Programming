def mergeSort(aList: list) -> list:
    # Divide
    # Base Case: Devide until, aList has only 1 element
    if len(aList) > 1:
        mid = len(aList) // 2
        print("midpoint ", mid)
        leftHalf = aList[:mid]
        rightHalf = aList[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        # At this point, 2 lists are ready to be merged while sorting
        return merge(aList, leftHalf, rightHalf)

def merge(resultList: list, leftHalf: list, rightHalf: list) -> list:
    print("merging ", leftHalf, rightHalf)

    # Iterate over both lists
    i, j, k = 0, 0, 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] < rightHalf[j]:
            resultList[k] = leftHalf[i]
            i += 1
            k += 1
        else:
            resultList[k] = rightHalf[j]
            j += 1
            k += 1
    
    # Left overs from LeftHalf
    while i < len(leftHalf):
        resultList[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        resultList[k] = rightHalf[j]
        j += 1
        k += 1

    # All elements from both lefthalf and righthalf are processed, sorted and kept in reulst
    print("result ", resultList)
    return resultList

aList = [5,1,3,2,4]
print(mergeSort(aList))