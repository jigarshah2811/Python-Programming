class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def remove_all_n(head, n):
    # Edge cases
    cur = head
    while cur.val == n:
        cur = cur.__next__
    newHead = cur
    print(("newHead: ", newHead.val))

    while cur.__next__ is not None:
        if cur.next.val == n:
            cur.next = cur.next.__next__
        cur = cur.__next__

    return newHead

head = ListNode(1, ListNode(2, ListNode(3)))
newHead = remove_all_n(head, 2)
print(newHead)
