# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        lis = []
        node = head
        while node:
            lis.append(node)
            node = node.next
        
        n = len(lis)
        k = int(math.ceil(n/2))
        i = 0
        while i < n:
            if i < k:
                if i == n-i-1:
                    lis[i].next = None
                else:
                    lis[i].next = lis[n-i-1]
            else:
                if i == n-i:
                    lis[i].next = None
                else:
                    lis[i].next = lis[n-i]
            i+=1
            
