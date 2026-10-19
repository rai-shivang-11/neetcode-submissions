# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def listsum(prev, curr1, curr2, carry):
            if not curr1 and not curr2 and (carry == 0): return
            val = (curr1.val if curr1 else 0)  + (curr2.val if curr2 else 0) + carry
            c =  val//10
            a = val%10
            node = ListNode(a)
            prev.next = node
            listsum(node, curr1.next if curr1 else None, curr2.next if curr2 else None, c)
        start = ListNode()
        listsum(start, l1, l2, 0)
        return start.next
            