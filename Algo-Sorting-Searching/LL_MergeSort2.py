class LinkedList:

    def __init__(self, item):
        self.item = item
        self.next = None

    def __insertAtEnd__(self, item):
        if self is None:
            # Create head
            self.__init__(item)
        current = self
        while current.__next__ is not None:
            current = current.__next__
        current.next = LinkedList(item)

    def MergeSort(self):
        if self is None or self.__next__ is None:
            return self

        # Split the list in sublists
        A, B = self.Split()

        # Sort indivudal lists
        A = A.MergeSort()
        B = B.MergeSort()

        # Merge sorted lists
        L = self.Merge(A, B)
        return L

    def Split(self):
        if self is None or self.__next__ is None:
            return self, None

        slow = self
        fast = self
        while fast is not None:
            fast = fast.__next__
            if fast.__next__ is not None:
                fast = fast.__next__
                slow = slow.__next__

        # Now slow is at Middle, & fast is at End of list
        # Split list in A & B sublists
        A = self
        B = slow.__next__
        slow.next = None
        return A, B

    def Print(self):
        print(self.item, " ", end=' ')
        if self.__next__ is not None:
            self.next.Print()
        else:
            print("\n")

    def Merge(self, A, B):
        # Base Case
        if A is None:
            return B
        if B is None:
            return A

        # Sort ele
        if A.item <= B.item:
            Result = A
            Result.next = self.Merge(A.__next__, B)
        else:
            Result = B
            Result.next = self.Merge(A, B.__next__)

        return Result


def main():
        L = LinkedList(3)
        L.__insertAtEnd__(1)
        L.__insertAtEnd__(5)
        L.__insertAtEnd__(9)
        L.__insertAtEnd__(7)
        L.__insertAtEnd__(2)
        L.__insertAtEnd__(4)
        L.Print()
        L = L.MergeSort()
        L.Print()
