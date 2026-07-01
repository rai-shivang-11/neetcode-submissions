# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def sumNode(prev, n1, n2, c):
            if not n1 and not n2:
                if c:
                    prev.next = ListNode(c)
                return
            s = c
            if n1: 
                s+= n1.val
                n1Next= n1.next
            else: 
                n1Next = None
            if n2: 
                s+= n2.val
                n2Next = n2.next
            else:
                n2Next = None
            total = s % 10
            carry = s // 10
            node = ListNode(total)
            prev.next = node
            sumNode(node, n1Next, n2Next, carry)
        
        head = ListNode(0)
        sumNode(head, l1, l2, 0)
        return head.next