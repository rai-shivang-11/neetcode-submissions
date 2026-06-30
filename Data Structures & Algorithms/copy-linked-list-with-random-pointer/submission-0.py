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
        nodes = {}
        def copy(n):
            if not n: return None
            if n in nodes: return nodes[n]
            node = Node(n.val, None, None)
            nodes[n] = node
            node.next = copy(n.next)
            node.random = copy(n.random)
            return node
        
        return copy(head)
