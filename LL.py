class Node(object):

    def __init__(self, item):
        self.item = item
        self.next = None


class DLLNode(object):

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None
"""
LL Tricks
1. Always check Current.next for condition, you have to mostly stop one node (current) before to operate upon
2. Where you can't check Current.next for condition, maintain prev
3. Head ?? validation
"""

class LinkedList:

    def __init__(self, item=0):
        self.head = Node(item)
        pass

    def insert(self, item):
        newNode = Node(item)
        if self.head is None:
            # 1st Node, Make it head
            self.head = newNode

        # Otherwise find end of list
        current = self.head
        while current.next is not None:
            current = current.next
        # We are at end of list, insert
        self.insertNode_Util(current, newNode)

    def insertNode_Util(self, current, newNode):
        # Link changes
        savedNext = current.next
        current.next = newNode
        newNode.next = savedNext

    def insertAtPosition(self, item, position):
        newNode = Node(item)
        if position == 0:
            self.head = newNode
        # edge case: what happens if position is given more than what list contains
        # Find the right pos to insert
        current = self.head
        i = 0
        while i < position-1:
            current = current.next
            i += 1
        # We are at pos, insert now
        self.insertNode_Util(current, newNode)

    def insertInSortedOrder(self, item):
        newNode = Node(item)

        # Head ??
        if self.head.item > item:
            self.insertNode_Util(self.head, newNode)

        # Search for right pos
        current = self.head
        while current.next.item < item:
            current = current.next
        self.insertNode_Util(current, newNode)

    def remove(self, item):
        # Head ??
        if self.head.item == item:
            newHeadRef = self.head.next
            del self.head
            self.head = newHeadRef
            return

        self.remove_node(Node(item))

    def remove_node(self, node):
        if isinstance(type(node), Node):
            return -1

        # Head with no next? Delete head with next is None!
        if self.head == node and self.head.next is None:
            del self.head

        current = self.head
        prev = self.head
        while current is not None and current.item != node.item:
            current = current.next
            prev = current

        # Tail ?
        if current is None:
            # Not found
            return -1
        elif current.next is None:
            # Tail node to be deleted
            prev.item = current.item
            prev.next = current.next
        else:
            # Regular node
            current.item = current.next.item
            current.next = current.next.next

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            savedNext = current.next

            # Reverse the link
            current.next = prev

            # Next iteration
            prev = current
            current = savedNext
        self.head = prev

    def detect_loop(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
                slow = slow.next
            if fast == slow:
                break

        # fast & slow are pointing at k nodes away from LoopNode
        # Head is         pointing at k nodes away from LoopNode
        current = self.head
        while current is not slow:
            current = current.next
            slow = slow.next

        return current

    def size(self, head=None):
        count = 0
        if head is None:
            current = self.head
        else:
            current = head

        while current is not None:
            count += 1
            current = current.next
        return count

    def size_recur_util(self, node):
        if node is None:
            return 0
        return 1 + self.size_recur_util(node.next)

    def size_recur(self):
        return self.size_recur_util(self.head)

    def printLL(self):
        current = self.head
        while current:
            print current.item,
            current = current.next

    def printLLReversed_Util(self, node):
        if node is None:
            return
        self.printLLReversed_Util(node.next)
        print node.item

    def printLLReversed(self):
        return self.printLLReversed_Util(self.head)

    def swap(self, item, new_item):
        current = self.head
        while current.item != item:
            if current.next is None:
                return False
            current = current.next
        # We are at node to swap
        current.item = new_item

    def middle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next
            if fast.next is not None:
                fast = fast.next
                slow = slow.next
        return slow

    def get_nth_from_last(self, n):
        slow = self.head
        fast = self.head
        while n > 0 and fast is not None:
            fast = fast.next
            n -= 1
        while fast is not None:
            fast = fast.next
            slow = slow.next
        return slow.item if fast is not None else -1

    def isPalindrom_Util(self, Left, Right):
        if Right is None:
            return True, Left

        # Left will be traversing reverse from back
        # Right will be traversing reverse from back
        isp, Left = self.isPalindrom_Util(Left, Right.next)
        if isp is False:
            return False, Left

        # Compare values of Right <-- with Left --->
        isp1 = (Left.item == Right.item)

        # Move Left
        Left = Left.next
        return isp1, Left

    def isPalindrom(self):
        Left = self.head
        Right = self.head
        return self.isPalindrom_Util(Left, Right)


"""
ADD 2 numbers represented as reversed LinkedList
https://leetcode.com/problems/add-two-numbers/description/
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Base Case
        # Base Case
        if l1 is None and l2 is None:
            if carry:
                return Node(carry)
            else:
                return None

        #1) Constraint for root
        sumVal = carry
        if l1 is not None:
            sumVal += l1.item
        if l2 is not None:
            sumVal += l2.item
        newNode = Node(sumVal % 10)

        # 2) Same constraint for next Node (Recurssion)
        newNode.next = self.addTwoNumbers(l1.next if l1 is not None else None,
                                          l2.next if l2 is not None else None,
                                          sumVal//10)
        return newNode



def addLL_Util_Reverse(node1, node2):
    # Base case
    # Return node values when both lists are empty
    if node1 is None and node2 is None:
        return None, 0

    headRef, carry = addLL_Util_Reverse(node1.next, node2.next)

    sum_nodes = carry + node1.item + node2.item
    newNode = Node(sum_nodes % 10)
    carry = sum_nodes // 10

    if headRef is None:
        headRef = newNode
    else:
        newNode.next = headRef
        headRef = newNode

    return headRef, carry


def intersection(L1, L2):
    m = L1.size()
    n = L2.size()
    if m > n:
        fast = L1
        slow = L2
    else:
        fast = L2
        slow = L1

    # Now SKIP abs(len(1)-len(2) nodes from bigger list
    for i in xrange(abs(m-n)):
        fast = fast.next

    # Now both list are same nodes away from INTERSECTION
    while slow != fast:
        fast = fast.next
        slow = slow.next

    return slow


def addLL(L1, L2):
    carry = 0
    return addLL_Util(L1, L2, carry)


def addLLReversed(L1, L2, sizeL1, sizeL2):
    skipNodes = abs(sizeL1 - sizeL2)
    while skipNodes > 0:
        L1 = L1.next
        skipNodes -= 1

    HeadRef, carry = addLL_Util_Reverse(L1, L2)
    return HeadRef


"""
Reverses a LL and returns Head of new LL
"""


def reverse(head):
    prev = None
    current = head
    while current is not None:
        savedNext = current.next

        # Reverse the link
        current.next = prev

        # Next iteration
        prev = current
        current = savedNext
    return prev


def main():
    myLL = LinkedList(1)
    myLL.insert(2)
    myLL.insert(3)
    myLL.insert(4)
    myLL.insert(5)

    reversed_head = reverse(myLL.head)
    while reversed_head is not None:
        print reversed_head.item
        reversed_head = reversed_head.next

    print "Adding 2 numbers represented by LL...."
    L1 = LinkedList(3)
    L1.insert(1)
    L1.insert(5)
    L1.insert(7)

    L2 = LinkedList(5)
    L2.insert(9)
    L2.insert(2)

    s = Solution()
    result = s.addTwoNumbers(L1.head, L2.head, 0)
    while result is not None:
        print result.item
        result = result.next

    """
    myLL = LinkedList('k')
    myLL.insert('a')
    myLL.insert('y')
    myLL.insert('a')
    myLL.insert('k')
    # myLL.printLL()

    print"\nChecking palindrome"
    isp, Left = myLL.isPalindrom()
    print isp

    myLL = None
    myLL = LinkedList(1)
    myLL.printLL()


    print "\nChecking insertInSortedOrder"
    myLL.insertInSortedOrder(4)
    myLL.printLL()

    print "\nChecking insertAtPosition"
    myLL.insertAtPosition(5, 3)
    myLL.printLL()

    print "\nChecking remove"
    myLL.remove(2)
    myLL.printLL()

    print "\nChecking remove HEAD"

    myLL.remove(1)
    myLL.printLL()

    print "\nChecking remove NOT FOUND"
    myLL.remove(15)
    myLL.printLL()

    print "\nChecking remove NOT FOUND"
    myLL.remove_node(Node(1))
    myLL.printLL()

    print "\nChecking remove"
    myLL.remove_node(Node(7))
    myLL.printLL()

    print "\nreverse"
    myLL.reverse()
    myLL.printLL()

    print "\nsize"
    print myLL.size()

    print "\nsize recur"
    print myLL.size_recur()

    print "\nreverse print"
    print myLL.printLLReversed()

    print "\nswap"
    myLL.swap(11, 5)
    myLL.printLL()

    print "\nmiddle"
    print myLL.middle().item

    print "get nth from last"
    print myLL.get_nth_from_last(3)
    """

if __name__ == "__main__":
    main()
