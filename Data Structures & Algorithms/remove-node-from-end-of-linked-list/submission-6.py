# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode
        prev.next = head
        self.c = 0
        def remove(prev, curr):
            if not curr: return
            remove(curr, curr.next)
            self.c += 1            
            if self.c == n:
                prev.next = curr.next
                return
        remove(prev, head)
        return prev.next