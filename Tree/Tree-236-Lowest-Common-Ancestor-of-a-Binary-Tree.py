# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node):
            if not node:
                return None
            
            if node.val == p.val or node.val == q.val:
                return node

            left = helper(node.left)
            right = helper(node.right)

            if right and left:
                return node
            
            return left or right
        
        return helper(root)