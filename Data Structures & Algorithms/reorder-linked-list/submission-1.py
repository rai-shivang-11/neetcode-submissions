# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lis = []
        while head:
            lis.append(head)
            head = head.next
        n = len(lis)-1
        sort = []
        i = 0
        while i <= (n//2):
            sort.append(lis[i])
            if (n-i) != i: sort.append(lis[n-i])
            i += 1
        dummy = curr = sort[0]
        for i in range(1,n+1):
            curr.next = sort[i]
            curr = sort[i]
        curr.next = None
        # return dummy
