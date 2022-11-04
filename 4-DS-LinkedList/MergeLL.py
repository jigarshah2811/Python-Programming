
from typing import Optional


class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0)   # Result List
        cur1, cur2 = list1, list2
        
        cur = newHead
        while cur1 and cur2:
            if cur1.val <= cur2.val: # Pick up cur1 node
                cur.next = cur1
                cur1 = cur1.next    # ---> list1
            else:
                cur.next = cur2
                cur2 = cur2.next    # ---> list2
            
            # ---> Result list
            print(f"Built: {cur.val}")
            cur = cur.next
        
        
        # One of the list is done now, add remaining nodes from the other list
        while cur1:
            cur.next = cur1
            cur = cur.next
            
        while cur2:
            cur.next = cur2
            cur = cur.next
        
        return newHead.next


    
s = Solution()

list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
list2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

s.mergeTwoLists(list1, list2)