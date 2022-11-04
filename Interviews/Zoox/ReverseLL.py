class Node:
        def __init__(self, val, next=None) -> None:
            self.val = val
            self.next = next
            # self.prev = prev  # Only in DLL

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        # self.tail = None    # Only in DLL

    def insert(self, listOfVals: list) -> Node:
        dummy = Node(0)
        prev, cur = None, dummy

        for val in listOfVals:
            cur.next = Node(val)
            prev, cur = cur, cur.next

        self.head = dummy.next
        return self.head

    def reverse(self) -> Node:
        prev, cur = None, self.head
        while cur:
            # Save cur's next and REVERSE the link
            savedNext = cur.next 
            cur.next = prev

            # ---> Move forward
            prev, cur = cur, savedNext

        self.head = prev
        return self.head
    
    def traverse(self):
        cur = self.head
        listOfVals = list()

        while cur:
            listOfVals.append(cur.val)    
            cur = cur.next

        print(listOfVals)

l1 = LinkedList()
print("Insert nodes in linkedlist")
l1.insert([1, 2, 3, 4, 5])
print("Traverse linkedlist")
l1.traverse()
print("Reverse linked list")
l1.reverse()
print("Traverse linkedlist")
l1.traverse()