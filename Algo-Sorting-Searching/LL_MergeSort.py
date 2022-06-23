# Python3 program merge two sorted linked
# in third linked list using recursive.


# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Constructor to initialize the node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Method to print linked list
    def printList(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.__next__

    # Function to add of node at the end.
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head

        while last.__next__:
            last = last.__next__
        last.next = new_node


class MergeSortLLSolution(object):
    def mergeSort(self, head):
        if head is None or head.__next__ is None:
            return head

        # Split unsorted list into A and B
        A, B = self.splitList(head)

        # A and B are 2 unsorted list. Split them until it becomes sorted (size=1)
        A = self.mergeSort(A)
        B = self.mergeSort(B)

        # A and B are SORTED. Now merge them
        return self.mergeLists(A, B)

    def splitList(self, head):
        slow = fast = head
        while fast:
            fast = fast.__next__
            if fast is not None:
                fast = fast.__next__
            slow = slow.__next__

        # Now, Fast is at End and Slow is at Middle
        A = head
        B = slow
        slow.next = None    # Break list into 2

        print(("Split A:{0}, B:{1}".format(A.data, B.data)))
        return A, B

    def mergeLists(self, A, B):
        dummy_head = Node(None)
        cur = dummy_head

        while A and B:
            if A.data < B.data:
                cur.next = A
                A = A.__next__
            else:
                cur.next = B
                B = B.__next__

        # Remaining of A or B
        if A is None:
            cur.next = A
        elif B is None:
            cur.next = B

        return dummy_head.__next__


if __name__ == '__main__':
    # Create linked list :
    # 10->20->30->40->50
    list1 = LinkedList()
    list1.append(3)
    list1.append(5)
    list1.append(7)

    # Create linked list 2 :
    # 5->15->18->35->60
    list2 = LinkedList()
    list2.append(1)
    list2.append(2)
    list2.append(4)
    list2.append(6)

    # Create linked list 3
    list3 = LinkedList()

    # Merging linked list 1 and linked list 2
    # in linked list 3
    #list3.head = mergeLists(list1.head, list2.head)

    print(" Merged Linked List is : ")
    list3.printList()

    print("Testing MergeSort")
    # Create linked list 4 :
    # 5->2->1->4->3
    list3 = LinkedList()
    list3.append(5)
    list3.append(2)
    list3.append(1)
    list3.append(4)
    list3.append(3)
    list3.printList()

    s = MergeSortLLSolution()
    s.mergeSort(list3.head)
