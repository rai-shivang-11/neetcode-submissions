# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        lis = []
        while curr:
            lis.append(curr)
            curr = curr.next
        target = len(lis) - n
        if n!=1 and target!=0:
            lis[target-1].next = lis[target+1]
        elif target == 0:
            if len(lis) > 1:
                return lis[1]
            else:
                return None
        else:
            lis[target-1].next = None
        return head