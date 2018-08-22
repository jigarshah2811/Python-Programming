# Python3 program merge two sorted linked
# in third linked list using recursive.

# Node class
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
            print temp.data
            temp = temp.next

    # Function to add of node at the end.
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next
        last.next = new_node

def splitList(head):
    slow = fast = head
    while fast:
        fast = fast.next
        if fast is not None:
            fast = fast.next
        slow = slow.next

    # Now, Fast is at End and Slow is at Middle
    A = head
    B = slow
    slow.next = None
    return A, B

def mergeSort(head):
    if head is None or head.next is None:
        return head

    # Split unsorted list into A and B
    A, B = splitList(head)

    # Indivudally sort A and B
    mergeSort(A)
    mergeSort(B)

    # Now we have 2 sorted lists, A & B, merge them
    return mergeLists(A, B)


# Function to merge two sorted linked list.
def mergeLists(A, B):
    tail  = None

    if A is None:
        return B
    if B is None:
        return A

    if A.data < B.data:
        tail = A
        tail.next = mergeLists(A.next, B)
    else:
        tail = B
        tail.next = mergeLists(A, B.next)

    return tail



# Driver Function
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
    list3.head = mergeLists(list1.head, list2.head)

    print(" Merged Linked List is : ")
    list3.printList()

    print "Testing MergeSort"
    # Create linked list 4 :
    # 5->2->1->4->3
    list3 = LinkedList()
    list3.append(5)
    list3.append(2)
    list3.append(1)
    list3.append(4)
    list3.append(3)
    sortedList = mergeSort(list3.head)
    sortedList.printList()