# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, node):
            if not node: return 0
            left = 1 + self.maxDepth(node.left)
            right = 1 + self.maxDepth(node.right)
            return max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
            if not root: return 0
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            diameter = left + right

            left = self.diameterOfBinaryTree(root.left)
            right = self.diameterOfBinaryTree(root.right)

            return  max(diameter, left, right)
