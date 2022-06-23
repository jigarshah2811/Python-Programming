class MergeSortSolution:
    def mergeSort(self, L):

        def mergeSortRecur(L):
            # Base case: Stop dividing when A size is 1
            if len(L) > 1:

                # 1) Divide array until size becomes 1
                mid = len(L) // 2
                A = L[:mid]
                B = L[mid:]
                mergeSortRecur(A)
                mergeSortRecur(B)
                merge(L, A, B)

        def merge(sortedList, A, B):
            a, b, i = 0, 0, 0

            while a < len(A) and b < len(B):
                if A[a] < B[b]:
                    sortedList[i] = A[a]
                    a += 1
                else:
                    sortedList[i] = B[b]
                    b += 1

                i += 1

            # Remaining in A or B
            while a < len(A):
                sortedList[i] = A[a]
                a += 1
                i += 1

            while b < len(B):
                sortedList[i] = B[b]
                b += 1
                i += 1

            print(sortedList)

        return mergeSortRecur(L)


s = MergeSortSolution()
inputList = [7, 3, 1, 2, 5, 6, 4]
s.mergeSort(inputList)
