class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, val=0):
        self.head = None

    def __append__(self, val):
        if self.head is None:
            self.head = self.Node(val)
            return

        # Append at the end of list
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = self.Node(val)

    """ Let's find out if this keyboard is working as expected254BTGBNBG  """
    def __insertAtPos__(self, pos, val):|
        cur = self.head
        while cur and pos > 1:
            pos -= 1
            cur = cur.next

        # Either we reached to pos or reached end
        newNode = self.Node(val)
        newNode.next = cur.next
        cur.next = newNode

    def __pop__(self):
        headVal = self.head.val
        self.head = self.head.next
        return headVal

    def __popAtPos__(self, pos):
        if self.head is None:  # Empty list
            raise IndexError

        cur = self.head
        while cur.next and pos > 0:
            cur = cur.next
            pos -= 1
        if cur.next is None:  # Trying to remove invalid index
            raise IndexError

        cur.next = cur.next.next

    def __remove__(self, val):
        if self.head is None:  # Empty list
            raise IndexError

        cur = self.head
        while cur.next and cur.next.val != val:
            cur = cur.next

        # cur is at point where next node is to be removed
        if cur.next is None:  # Trying to remove invalid index
            raise IndexError

        cur.next = cur.next.next

    def __hasNext__(self):
        return self.cur is None

    def __print__(self):
        cur = self.head
        while cur:
            print(cur.val,)
            cur = cur.next
