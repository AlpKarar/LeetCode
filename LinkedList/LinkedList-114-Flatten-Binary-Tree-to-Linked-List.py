# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return
        
        res = []

        def helper(root):
            if not root:
                return
            
            res.append(root)

            helper(root.left)
            helper(root.right)
        
        helper(root)

        for i in range(len(res) - 1):
            res[i].right = res[i+1]
            res[i].left = None
        
        res[-1].right = None
        res[-1].left = None