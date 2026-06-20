# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        newHead = head              #Fallbackn incase of only one value in the list

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head   #Pointing the next element's next back to the prevcious element
        head.next = None            #Set to None for the last element of the list, rest of them get overwritten

        return newHead