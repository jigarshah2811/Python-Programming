def mergeSort(L):

    if len(L) > 1:
        print "Spliting ", L
        mid = len(L) // 2
        lefthalf = L[:mid]
        righthalf = L[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        merge(lefthalf, righthalf, L)


def merge(lefthalf, righthalf, L):
    i = 0
    j = 0
    k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            L[k] = lefthalf[i]
            i += 1
        else:
            L[k] = righthalf[j]
            j += 1
        k += 1

    while i < len(lefthalf):
        L[k] = lefthalf[i]
        i += 1
        k += 1

    while j < len(righthalf):
        L[k] = righthalf[j]
        j += 1
        k += 1
    print "Merging ", L


def main():
    L = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(L)
    print(L)


if __name__ == "__main__":
    main()