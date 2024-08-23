# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = dict()

        def helper(root, i):
            if not root:
                return
            
            if i % 2 != 0:
                levels[i] = levels.get(i, []) + [root]
            
            helper(root.left, i + 1)
            helper(root.right, i + 1)
        
        helper(root, 0)

        for level in levels:
            l = 0
            r = len(levels[level]) - 1

            while l < r:
                levels[level][l].val, levels[level][r].val = levels[level][r].val, levels[level][l].val
                l += 1
                r -= 1
        
        return root
