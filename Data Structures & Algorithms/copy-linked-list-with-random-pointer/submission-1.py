"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        self.copies = {}
        prev = Node(0)
        def duplicate(prev, curr):
            if not curr:
                prev.next = None
                return
            copy = Node(curr.val)
            prev.next = copy
            self.copies[curr] = copy
            duplicate(copy, curr.next)
            copy.random = self.copies[curr.random] if curr.random else None
            return
        duplicate(prev, head)
        return prev.next