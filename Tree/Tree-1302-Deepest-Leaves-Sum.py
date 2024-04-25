# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        res = [0, 0] # []
        
        def helper(root, depth):
            if not root:
                return
            
            if not root.left and not root.right:
                if depth > res[0]:
                    res[0] = depth
                    res[1] = root.val
                elif depth == res[0]:
                    res[1] += root.val
            
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)
        
        helper(root, 0)

        return res[1]