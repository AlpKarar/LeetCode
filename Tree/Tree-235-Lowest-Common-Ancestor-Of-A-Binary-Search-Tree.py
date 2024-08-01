# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findNodes(node):
            if not node:
                return None
            
            if node == p or node == q:
                return node
            
            left = findNodes(node.left)
            right = findNodes(node.right)

            if (left == p or right == p) and (left == q or right == q):
                return node

            return left or right
        
        return findNodes(root)