# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            if not list2: return None
            else: return list2
        if not list2:
            if not list1: return None
            else: return list1
        
        def merge(list1, list2, prev):
            if not list1:
                if not list2: 
                    return None
                else:
                    prev.next = list2
                    return None
            if not list2:
                if not list1: 
                    return None
                else:
                    prev.next = list1
                    return None
            if list1.val < list2.val:
                prev.next = list1
                prev= list1
                merge(list1.next, list2, prev)
            else:
                prev.next = list2
                prev= list2
                merge(list1, list2.next, prev)
        
        if list1.val < list2.val:
            head = list1
            prev = list1
            merge(list1.next, list2, prev)
        else:
            head = list2
            prev = list2
            merge(list1, list2.next, prev)
        return head
