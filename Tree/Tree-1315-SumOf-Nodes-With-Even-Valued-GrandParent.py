# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        

        def helper(root):
            if not root:
                return 0
            
            curTotal = 0

            if root.val % 2 == 0:
                if root.left:
                    if root.left.left:
                        curTotal += root.left.left.val
                    
                    if root.left.right:
                        curTotal += root.left.right.val
                
                if root.right:
                    if root.right.left:
                        curTotal += root.right.left.val
                    
                    if root.right.right:
                        curTotal += root.right.right.val
            
            return helper(root.left) + helper(root.right) + curTotal
    
        return helper(root)