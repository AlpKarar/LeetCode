# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        m = [root, 0]

        def helper(root, level):
            if not root:
                return
            
            if level > m[1]:
                m[0] = root
                m[1] = level
                  
            helper(root.left, level + 1)
            helper(root.right, level + 1)
        
        helper(root, 0)

        return m[0].val   